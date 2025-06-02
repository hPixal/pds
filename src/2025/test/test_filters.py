import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
import tkinter as tk
from tkinter import filedialog, messagebox

# Helper functions
def play_audio(data, samplerate):
    sd.stop()
    sd.play(data, samplerate)

def load_audio_file(filename):
    data, samplerate = sf.read(filename)
    if data.ndim > 1:
        data = data.mean(axis=1)  # Convert to mono if stereo
    return data, samplerate

def save_audio_file(filename, data, samplerate):
    sf.write(filename, data, samplerate)

def butterworth_filter(spectrum, w_o, n, type='low', a_0 = 1):
    N = len(spectrum)
    freqs = np.fft.fftfreq(N)
    H = np.ones(N)

    if type == 'low':
        H = a_0 / (1 + (np.abs(freqs) / w_o) ** (2 * n))
    elif type == 'high':
        H = a_0 / (1 + (w_o / np.abs(freqs + 1e-12)) ** (2 * n))
    else:
        raise ValueError("type must be 'low' or 'high'")

    return spectrum * H

def apply_filter(audio_data):

    audio_array = np.array(audio_data)
    
    # Original frequency
    fft_data = np.fft.fft(audio_array)
    fft_magnitude = np.abs(fft_data)
    
    # Filtered frequency
    fft_filtered = butterworth_filter(fft_data, 0.02, 2,'high')  # Use a normalized cutoff (e.g., 0.2)
    filtered_audio = np.fft.ifft(fft_filtered).real
    fft_filtered_magnitude = np.abs(fft_filtered)
    
    fftrq = np.fft.fftfreq(len(fft_magnitude))
    
    fig, axs = plt.subplots(2, 2, figsize=(14, 8))

    # FFT Magnitude Spectrum (Original)
    axs[0, 0].plot(fftrq, fft_magnitude)
    axs[0, 0].set_title("Original FFT Magnitude Spectrum")
    axs[0, 0].set_xlabel("Frequency Bin")
    axs[0, 0].set_ylabel("Magnitude")

    # Audio Waveform (Original)
    axs[1, 0].plot(audio_array)
    axs[1, 0].set_title("Original Audio Waveform")
    axs[1, 0].set_xlabel("Sample Index")
    axs[1, 0].set_ylabel("Amplitude")

    # FFT Magnitude Spectrum (Filtered)
    axs[0, 1].plot(fftrq, fft_filtered_magnitude)
    axs[0, 1].set_title("Filtered FFT Magnitude Spectrum")
    axs[0, 1].set_xlabel("Frequency Bin")
    axs[0, 1].set_ylabel("Magnitude")

    # Audio Waveform (Filtered)
    axs[1, 1].plot(filtered_audio)
    axs[1, 1].set_title("Filtered Audio Waveform")
    axs[1, 1].set_xlabel("Sample Index")
    axs[1, 1].set_ylabel("Amplitude")

    plt.tight_layout()
    plt.show()
    return filtered_audio
    

# GUI
class AudioFilterApp:
    def __init__(self, master):
        self.master = master
        master.title("Digital Filter Playground")

        self.audio_file = None
        self.audio_data = None
        self.samplerate = None
        self.filtered_data = None

        self.load_button = tk.Button(master, text="Load Audio", command=self.load_audio)
        self.load_button.pack(pady=5)

        self.play_original_button = tk.Button(master, text="Play Original", command=self.play_original, state=tk.DISABLED)
        self.play_original_button.pack(pady=5)

        self.play_filtered_button = tk.Button(master, text="Play Filtered", command=self.play_filtered, state=tk.DISABLED)
        self.play_filtered_button.pack(pady=5)

    def load_audio(self):
        filetypes = [("MP3 files", "*.mp3"),("MP4 files", "*.mp4"),("WAV files", "*.wav"), ("All files", "*.*")]
        filename = filedialog.askopenfilename(initialdir=".", filetypes=filetypes)
        if filename:
            try:
                self.audio_data, self.samplerate = load_audio_file(filename)
                self.filtered_data = apply_filter(self.audio_data.copy())
                self.audio_file = filename
                self.play_original_button.config(state=tk.NORMAL)
                self.play_filtered_button.config(state=tk.NORMAL)
                messagebox.showinfo("Loaded", f"Loaded {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not load audio: {e}")

    def play_original(self):
        if self.audio_data is not None:
            play_audio(self.audio_data, self.samplerate)

    def play_filtered(self):
        if self.filtered_data is not None:
            play_audio(self.filtered_data, self.samplerate)

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioFilterApp(root)
    root.mainloop()
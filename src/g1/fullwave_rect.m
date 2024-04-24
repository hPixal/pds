function x = fullwave_rect(x)
    avg = sum(x)/length(x);
    for i = 1:length(x)
        if x(i) < avg
            x(i) = avg + abs(x(i) - avg);
        endif
    endfor
end
function x = quantization(n,x)
    ymax = max(x);
    ymin = min(x);
    dy = (ymax - ymin) / n;
    x = round((x - ymin) / dy) * dy + ymin;
end
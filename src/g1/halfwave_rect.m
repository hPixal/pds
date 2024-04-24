function [x] = halfwave_rect(x)
    avg = sum(x)/length(x);
    for i = 1:length(x)
        if x(i) < avg
            x(i) = avg;
        endif
    endfor
end
function ans = e2()
    t = -1:0.01:1;
    x = sinc(t);

    x = quantization(8,x);
    h = plot(t,x);
    waitfor(h);

    t = -(2*3.1416):0.01:(2*3.1416);
    x = sin(t);

    x = halfwave_rect(x);
    h = plot(t,x);
    waitfor(h);

    t = -(2*3.1416):0.01:(2*3.1416);
    x = sin(t);

    x = fullwave_rect(x);
    h = plot(t,x);
    waitfor(h);
end
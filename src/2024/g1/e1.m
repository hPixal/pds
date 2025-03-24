function ans = e1()
    [t,x] = sinusoidal(-1,1,5,100,1,0);
    length(t)
    length(x)
    h = stem(t,x);
    waitfor(h);

    [t,x] = sync(-1,1,5,100,1);
    length(t)
    length(x)
    h = stem(t,x);
    waitfor(h);

    [t,x] = square(-1,1,5,100,1,0);
    length(t)
    length(x)
    h = plot(t,x);
    waitfor(h);
end;
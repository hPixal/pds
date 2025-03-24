function e3 = e3()
    Tm = 0.00125; A = -3; f = 20;
    lambda = 0.0425-0.0325;
    t = 0:Tm:0.1-Tm;
    T = 0.05;
    phi = 0.729727+2*pi*f*4.4*T/16;
    x = @(t) A*sin(2*pi*f*t + phi);
    h = stem(t,x(t));
    waitfor(h)
end 
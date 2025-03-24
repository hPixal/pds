function res = e5()
    f = 4000;
    ti = 0; tf = 2;
    fm = 129;
    dt = 1/fm; phi = 0;
    t = ti:dt:tf; A = 2;

    x = @(t) A*sin(2*pi*f*t + phi);
    h = stem(t,x(t));
    waitfor(h)
end 
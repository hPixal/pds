function res = e4()
    f = 5; 
    ti = 0; tf = 1;
    fm = 100; % 25 10 4 1 0.5
    dt = 1/fm; phi = 0;
    t = ti:dt:tf; A = 2;
    
    x = @(t) A*sin(2*pi*f*t + phi);
    h = stem(t,x(t));
    waitfor(h)
end 
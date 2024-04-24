function [t,x] = square(t_i,t_f,freq,n,a,phi)
    dt = abs(t_f-t_i) / n ;
    t = t_i:dt:t_f-dt;

    x = a*sign(sin(t*freq*2*3.1416 + phi));
    
end
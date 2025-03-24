function res = e7()
    tini = 0;
    tfin = 1;
    fm = 80; 
    T = 1/fm;
    t = tini:T:tfin-T;
    
    length(t);
    





    means = [];
    vars = [];

    for i = 1:30
        y = randn(1 , length(t));
        means(end+1) = mean(y);
        vars(end+1) = var(y);
    end
    res = 1;

    means = mean(means)
    vars = var(vars)

    h = hist(y, 10);  % Especificar el número de bins con un par nombre-valor

    % Agregar títulos y etiquetas
    title('Histograma de datos');
    xlabel('Valor');
    ylabel('Frecuencia');

    


    %h = stem(t,y);
    waitfor(h)
    

end 
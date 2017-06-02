n = 100000;
t = zeros(n,1);
for i = 1:n
    index = 0;
    total = 0;
    while(1)
        x = ceil(rand()*6);
        total = total + x;
        index = index +1;
        if total >= 300
            break;
        end
    end
    t(i,1) = index;
    
    
end
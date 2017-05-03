x = 5;
s = 3;
m = 6;
p_ar = 1/((2*pi)^0.5*s)*exp(-(x-m)^2/(2*s^2));


n = 100000000;
bit = zeros(n,1);
bitV = zeros(n,1);
bitV5 = zeros(n,1);
for i = 1:n
    if rand()<0.5832
        bit(i,1) = 1;
        bitV(i,1) = randn()*3 + 6;
    else
        bit(i,1) = 0;
        bitV(i,1) = randn()*2 + 4;
    end
    
    if 4.999<bitV(i,1) && bitV(i,1)<5.001
        bitV5(i,1) = 1;
    end
    
end 
sum(bitV5)
b = (~bit) & bitV5;
sum(b)
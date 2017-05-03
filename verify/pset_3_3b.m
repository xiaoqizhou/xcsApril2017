l = 1000000;

filp = zeros(l,1);
n = 4;
p = 0.05;
for i = 1:l
    bitStream = zeros(1,2*n);
    for j = 1:2*n
        if rand()< p
            bitStream(j) = 1;
        end
    end
    filp(i,1) = any(bitStream(1:8)~=0) & any(bitStream(1:4)~=bitStream(5:8));
    
    
end

output = sum(filp)/l;
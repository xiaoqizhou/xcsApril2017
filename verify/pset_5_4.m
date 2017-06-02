n = 100000;
x = zeros(n,1);
y = zeros(n,1);
for i = 1:n
    index = ceil(rand()*6);
    x(i,1) = index;
    y(i,1) = index^2;
end

output = cov(x,y);
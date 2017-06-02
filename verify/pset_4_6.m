total = zeros(100000,1);
for i = 1:100000
    x = rand()*10 - 5;
    y = rand()*10 - 5;
    total(i,1) = abs(x)+abs(y);
end
result = mean(total);
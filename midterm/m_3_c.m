n = 100000;
correct = zeros(n,1);
output = 0;
for i = 1:n
    correct(i,:) = 0;
    for j = 1:10000
        if rand()<0.2
            correct(i,:) = correct(i,:) + 1;
        end
    end
    
    if correct(i,:) > 2000
        output = output + 1;
    end
end
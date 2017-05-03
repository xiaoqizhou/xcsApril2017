n = 1000000;
failN = zeros(n,1);

fail2 = zeros(n,1);

lambda = zeros(n,1);
for i = 1:n
    if rand()<0.75
        failN(i,1) = random('Poisson', 3);  
        lambda(i,1) = 3;
    else
        failN(i,1) = random('Poisson', 5);
        lambda(i,1) = 5;
    end
    
end

fail2 = failN == 2;
lambda3 = lambda == 3;

fail2_l3 = fail2 & lambda3;

output = sum(fail2_l3)/sum(fail2);
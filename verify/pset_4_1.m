r = poissrnd(5.5*3, 10000,1);
a = find(r > 15.5);
pd = makedist('Normal', 5.5*3, (5.5*3)^0.5);
y = cdf(pd,15.5);

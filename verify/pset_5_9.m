n = 100000;

ax = randn(n,20)*10 + 50;
bx = randn(n,20)*(200^0.5) + 52;
a = mean(ax,2)*20;
b = mean(bx,2)*20;
c = a - b;

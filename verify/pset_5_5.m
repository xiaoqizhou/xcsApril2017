n = 100000;
x = randn(n,1)*(2^0.5)+1;
y = randn(n,1)*(2^0.5)+1;

z = 2*x+y ;
[mu,sigma,muci,sigmaci] = normfit(z);
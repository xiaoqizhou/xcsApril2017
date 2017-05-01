muA = polls(:,2).*polls(:,4)./polls(:,1);
sumMuA = sum(muA);
muB = polls(:,3).*polls(:,4)./polls(:,1);
sumMuB = sum(muB);
sigma = 1/((sum(polls(:,1)))^0.5)*350;
sigma_2 = sigma^2;

aWin = 0;
for i = 1:1000000
    sA = randn()*sigma + sumMuA;
    sB = randn()*sigma + sumMuB;
    if sA > sB
        aWin = aWin + 1;
    end
        
end
sumMuA = sum(polls(:,2)./polls(:,1));
muA = sumMuA/10;
sumMuB = sum(polls(:,3)./polls(:,1));
muB = sumMuB/10;
sigmaA = std(polls(:,2)./polls(:,1))*4.5;
sigmaB = std(polls(:,3)./polls(:,1))*4.5;
sigmaA_2 = sigmaA^2;
sigmaB_2 = sigmaB^2;
aWin = 0;
for i = 1:100000
    sA = randn()*sigmaA + muA;
    sB = randn()*sigmaA + muB;
    if sA > sB
        aWin = aWin + 1;
    end
        
end
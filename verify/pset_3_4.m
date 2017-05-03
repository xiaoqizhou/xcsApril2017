output = 0;
for i = 0:4
    output = output + factorial(12)/(factorial(12-i)*factorial(i))*0.9^i*0.1^(12-i)
end

n = 1000000;

result = zeros(n,1);
jury = 12;
totalG = 0;
for i = 1:n
    if rand()<0.75
        defendant = 1;
        voteI = 0.2;
    else
        defendant = 0;
        voteI = 0.9;
    end
    vote = zeros(1,jury);
    for j = 1:jury
        if rand()<voteI
            vote(j) = 0;
        else
            vote(j) = 1;
        end
    end
    if sum(vote) >= 9
        voteResult = 1;
        totalG = totalG + 1;
    else
        voteResult = 0;
    end
    
    if voteResult == defendant
        result(i,1) = 1;
        
    else
        result(i,1) = 0;
        
    end
    
        
    
    
    
end

correctRate = sum(result)/n;
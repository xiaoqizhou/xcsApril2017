n = 100000;
numList = zeros(n,10);
good = 0;
for i = 1:n
    numList(i,:) = randperm(10);
    index = find(numList(i,:) == 1);
    good1 = 0;
    if index > 1 && index < 10
        if numList(i,index+1 ) == 2 || numList(i,index-1 ) == 2
            good1 = 1;
        end
    elseif index == 1
        
        if numList(i,index+1 ) == 2 
            good1 = 1;
        end
    else
        
        if numList(i,index-1 ) == 2 
            good1 =  1;
        end
    end
    
    index = find(numList(i,:) == 3);
    good2 = 0;
    if index > 1 && index < 10
        if numList(i,index+1 ) == 4 || numList(i,index-1 ) == 4
            good2 = 1;
        end
    elseif index == 1
        
        if numList(i,index+1 ) == 4 
            good2 = 1;
        end
    else
        
        if numList(i,index-1 ) == 4 
            good2 = 1;
        end
    end
    if good1 + good2 > 0
        good = good + 1;
    end
end
n = 1000;
numList = zeros(n,10);
good = 0;
for i = 1:n
    numList(i,:) = randperm(10);
    index = find(numList(i,:) == 1);
    numList_now = numList(i,:);
    if index > 1 && index < 10
        if numList(i,index+1 ) == 2 || numList(i,index-1 ) == 2
            good = good + 1;
        end
    elseif index == 1
        
        if numList(i,index+1 ) == 2 
            good = good + 1;
        end
    else
        
        if numList(i,index-1 ) == 2 
            good = good + 1;
        end
    end
end
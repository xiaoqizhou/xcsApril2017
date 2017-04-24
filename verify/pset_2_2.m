n = 100000;
c = 2;
for i = 1:n
    cardList = 1:52;
    for j = 1:c
        a= round(rand()*size(cardList,2)+0.5);
        result(i,j) = cardList(a);
        cardList(a) = [];
    end
        
    if all(result(i,:) < 5)
        output(i,1) = 1;
    else
        output(i,1) = 0;
    end

    if any(result(i,:) == 1)
        output(i,2) = 1;
    else
        output(i,2) = 0;
    end


    if any(result(i,:) < 5)
        output(i,3) = 1;
    else
        output(i,3) = 0;
    end
    
    
end


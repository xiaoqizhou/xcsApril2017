n = 100000;
c = 3;

serverP = [zeros(1,55), ones(1,45)];


for i = 1:n
    for j = 1:5

            cardList = serverP(1,:);
            a= round(rand()*size(cardList,2)+0.5);
            result(i,j) = cardList(a);
    end

    if any(result(i,1:5) == 1)
        output(i,1) = 1;
    else
        output(i,1) = 0;
    end  
    if sum(result(i,1:5)) == 3
        output(i,2) = 1;
    else
        output(i,2) = 0;
    end
    if sum(result(i,1:5)) >= 3
        output(i,3) = 1;
    else
        output(i,3) = 0;
    end  
    
end

pAll = sum(output)/n;

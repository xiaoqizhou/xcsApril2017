n = 100000;
c = 3;
movieP(1,:) = [zeros(1,28), ones(1,72)];
movieP(2,:) = [zeros(1,55), ones(1,45)];
movieP(3,:) = [zeros(1,13), ones(1,87)];

movieQ(1,:) = [zeros(1,80), ones(1,20)];
movieQ(2,:) = [zeros(1,40), ones(1,60)];
movieQ(3,:) = [zeros(1,5), ones(1,95)];
T(1,:) = [zeros(1,40), ones(1,60)];
for i = 1:n
    cardList = T;
    a= round(rand()*size(cardList,2)+0.5);
    result(i,4) = cardList(a);
    for j = 1:c
        if result(i,4) == 1
            cardList = movieP(j,:);
            a= round(rand()*size(cardList,2)+0.5);
            result(i,j) = cardList(a);
        else
            cardList = movieQ(j,:);
            a= round(rand()*size(cardList,2)+0.5);
            result(i,j) = cardList(a);
        end
    end
    
    if result(i,1) == 1 && result(i,4) == 1
        output(i,1) = 1;
    else
        output(i,1) = 0;
    end
    
    if result(i,2) == 1 && result(i,4) == 1
        output(i,2) = 1;
    else
        output(i,2) = 0;
    end  
    
    if result(i,3) == 1 && result(i,4) == 1
        output(i,3) = 1;
    else
        output(i,3) = 0;
    end       

    if result(i,1) == 1 && result(i,4) ~= 1
        output(i,4) = 1;
    else
        output(i,4) = 0;
    end
    
    if result(i,2) == 1 && result(i,4) ~= 1
        output(i,5) = 1;
    else
        output(i,5) = 0;
    end  
    
    if result(i,3) == 1 && result(i,4) ~= 1
        output(i,6) = 1;
    else
        output(i,6) = 0;
    end  
    
    if all(result(i,1:3) == 1) && result(i,4) == 1
        output(i,7) = 1;
    else
        output(i,7) = 0;
    end 
    
    if any(result(i,1:3) == 1) && result(i,4) == 1
        output(i,8) = 1;
    else
        output(i,8) = 0;
    end
    
    if result(i,4) == 1
        output(i,9) = 1;
    else
        output(i,9) = 0;
    end 
    
    if all(result(i,1:3) == 1)
        output(i,10) = 1;
    else
        output(i,10) = 0;
    end  
    
    
end

pAll = sum(output)/n;

p1 = pAll(1)/pAll(9);
p2 = pAll(2)/pAll(9);
p3 = pAll(3)/pAll(9);

q1 = pAll(4)/(1-pAll(9));
q2 = pAll(5)/(1-pAll(9));
q3 = pAll(6)/(1-pAll(9));

a1 = pAll(7)/pAll(9);
a2 = pAll(8)/pAll(9);
a3 = pAll(7)/pAll(10);

b1 = p1*p2*p3;
b2 = p1+p2+p3 - p1*p2-p1*p3-p3*p2 + p1*p2*p3;
b3 = 0.6*p1*p2*p3/(0.6*p1*p2*p3 + 0.4*q1*q2*q3);
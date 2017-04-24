n = 500000;
index = 0;
for i = 1:n
    s = 0;
    while(s < 100)
        a = round(rand()*100+0.5);
        index = index+1;
        b(index) = a;
        s = s+a;
    end
    last(i,1) = a;
    while(s < 200)
        a = round(rand()*100+0.5);
        index = index+1;
        b(index) = a;
        s = s+a;
    end
    last(i,2) = a;
    
    if last(i,1) > last(i,2)
        result(i,1) = 1;
    elseif last(i, 1) < last(i,2)
        result(i,1) = 2;
    else
        result(i,1) = 0;
    end
    
end

counts = hist(result);
countsAll = hist(b,0:100);
figure(1)
hist(last(:,1),1:100);
figure(2)
hist(last(:,2),1:100);
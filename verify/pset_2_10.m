n = 1000000;

colorF = [0,1];
colorM = [0,1];
colorW = zeros(n,2);
colorC = zeros(n,2);
colorS = zeros(n,2);
colorD = zeros(n,2);
result_color = zeros(n,3);
result = zeros(n,5);
for i = 1:n
    
    
    cardList = colorF;
    a= round(rand()*size(cardList,2)+0.5);
    F = cardList(a);
    
    cardList = colorM;
    a= round(rand()*size(cardList,2)+0.5);
    M = cardList(a);
    
    colorW(i,:) = [F,M];
    
    cardList = colorF;
    a= round(rand()*size(cardList,2)+0.5);
    F = cardList(a);
    
    cardList = colorM;
    a= round(rand()*size(cardList,2)+0.5);
    M = cardList(a);
    
    colorC(i,:) = [F,M];
    
    cardList = colorW(i,:);
    a= round(rand()*size(cardList,2)+0.5);
    W = cardList(a);
    
    colorS(i,:) = [W, 1];
    cardList = colorW(i,:);
    a= round(rand()*size(cardList,2)+0.5);
    W = cardList(a);
    
    
    colorD(i,:) = [W, 1];
    
    result_color(i,1) = colorW(i,1)*colorW(i,2);
    result_color(i,2) = colorS(i,1)*colorS(i,2);
    result_color(i,3) = colorD(i,1)*colorD(i,2);
    result_color(i,4) = colorC(i,1)*colorC(i,2);
    
    if result_color(i,4) == 1 && result_color(i,1) == 0
        result(i,1) = 1;
    else
        result(i,1) = 0;
    end
    
    if result_color(i,4) == 1 && result_color(i,1) == 0 && any(colorW(i,:) == 1)
        result(i,2) = 1;
    else
        result(i,2) = 0;
    end
    
    if result_color(i,4) == 1 && result_color(i,1) == 0 && result_color(i,2) ==1
        result(i,3) = 1;
    else
        result(i,3) = 0;
    end
    
    if result_color(i,4) == 1 && result_color(i,1) == 0 && result_color(i,2) ==0 && result_color(i,3) == 0
        result(i,4) = 1;
    else
        result(i,4) = 0;
    end
    
    if result_color(i,4) == 1 && result_color(i,1) == 0 && result_color(i,2) ==0
        result(i,5) = 1;
    else
        result(i,5) = 0;
    end
    
    
end

output = sum(result(:,4))/sum(result(:,5));
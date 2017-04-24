n = 1000000;

locationP = [1,2,2,3,4,5,6,6,7,8,9,10,11,11,12,13,14,15,15,16];

BP = [0.75, 0.95,0.75, 0.05, 0.05, 0.75, 0.95, 0.75, 0.01, 0.05, 0.75, 0.95, 0.01, 0.01, 0.05, 0.75];

result = zeros(n, 2);

result_location = zeros(n, 16);

for i = 1:n
    
    
    cardList = locationP(1,:);
    a= round(rand()*size(cardList,2)+0.5);
    location = cardList(a);
    
    if rand() <BP(location)
        result(i,location) = 1;
    else
        result(i,location) = 0;
    end    
end

output = sum(result)/sum(result(:));
n = 1000000;
x = 4096;
money = zeros(n,1);
for i = 1:n
    tail = 0;
    head = 0;
    while(tail == 0)
        if rand() < 0.5
            head = head + 1;
        else
            tail  =tail + 1;
        end
    end
    money(i,1) = min(2^head,x);
    
end

output = sum(money)/n;
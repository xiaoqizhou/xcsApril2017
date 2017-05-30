
n = 100000;
x = zeros(n,1);
z = zeros(n,1);
y = zeros(n,1);


tt = 0;
for i = 1:n
    total = 0;
    total_2 = 0;
    index = 0;
    while(true)
        roll = ceil(rand()*6);

        total = total + roll;
        total_2 = total_2 + 1;
        if (roll >= 3)
            if index == 0
                tt = tt + 1;
            end
            break;
        end
        index = index + 1;
    end

    x(i,1) = total;
    z(i,1) = roll;
    y(i,1) = total_2;
end


mean(x)
mean(z)
mean(y)
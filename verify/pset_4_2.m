total = 0;
for x = 0:0.001:1
    for y = 0:0.001:1
        if y < x
            total = total + 0.001^2*4*y/x*y;
        end
    end
end
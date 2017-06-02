total_a = 0;
for i = 10:0.00001:30
    total_a = total_a + 0.00001*0.043/i;
end

total_b = 0;
for i = 7.5:0.00001:30
    total_b = total_b + 0.00001*7.2/i^3;
end

total_c = 0;
for i = 7.5:0.00001:30
    total_c = total_c + 0.00001*0.043/i*i;
end

total_d = 0;
for i = 7.5:0.00001:30
    total_d = total_d + 0.00001*7.2/i^3*i;
end

total_e = 0;
for i = 7.5:0.00001:30
    total_e = total_e + 0.00001*0.043/i*i^2;
end

total_f = 0;
for i = 7.5:0.00001:30
    total_f = total_f + 0.00001*7.2/i^3*i^2;
end
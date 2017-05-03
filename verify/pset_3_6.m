n = 100000;
m = 8;
p = [0.1,0.2,0.1,0.35,0.05, 0.03,0.17];
result = zeros(n,1);
for i = 1:n
    result_now = zeros(1,size(p,2));
    for k = 1:m
    pp = rand();

    for j = 1:size(p,2)
        pp = pp - p(j);
        if pp < 0
            break;
        end
    end
    result_now(j) = result_now(j)+1;
    end
    result(i,1) = sum(result_now > 0);
end
output = 0;
for i = 1:size(p,2)
    output = output + (1-(1-p(i))^m);
end
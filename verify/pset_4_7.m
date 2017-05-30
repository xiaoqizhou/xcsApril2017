arr_max = zeros(100000,1);
for n = 1:100000
    arr = rand(12, 1)*100000000;
    arr_max_m = -1;
    for i = 1:size(arr,1)
        if arr(i,1) > arr_max_m
            arr_max_m = arr(i,1);
            arr_max(n,1) = arr_max(n,1)+1;
        end
    end
end
e_max = mean(arr_max);
tt = 0;
for i = 1:12
    tt = tt+1/i;
end
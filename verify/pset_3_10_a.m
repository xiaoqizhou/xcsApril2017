function output = pset_3_10_a()

n = 1000000;
output = zeros(n,1);
for i = 1:n
    output(i,1) = bb(1:10, ceil(rand()*10));

end

end

function output = aa(arr, key)

for i = 1:10
    if (arr(i) == key)
        output =  i-1;
        return;
    end
end
output = -1;
return;
end

function output = bb(arr, key)
low = 0;
high = 9;
while (low <= high)
    mid = round((low+high)/2);
    if (arr(mid + 1) == key)
        output = mid;
        return;
    elseif arr(mid+1) < key
        low = mid+ 1;
    else
        high = mid -1;
    end
end

    output = -1;
    return;
end
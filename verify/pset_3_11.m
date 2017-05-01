
if 0
    output = 0;
    aa = [];
    total = 0;
    for i = 0:20
        aa(i+1) = exp(-9)*9^i/(factorial(i))
        output = output + exp(-9)*9^i/(factorial(i));
        total = total+aa(i+1)*i;
    end
end

if 1
    m = 24000;
    n = 8000;
    kk = 3;
    lo = 100000;
    bitListSum = zeros(lo,1);
    correctList = ones(lo, 1);
    bitOneSum = zeros(lo,1);
    for loop = 1:lo
        fprintf('%d\n',loop);
        bitList = zeros(n,1);
        for i = 1:m
            for j = 1:kk
                x = floor(rand()*n)+1;
                bitList(x) = 1;
                if x == 1
                    bitOneSum(loop,1) = bitOneSum(loop,1)+1;
                end
            end
        end
        for j = 1:kk
            x = floor(rand()*n)+1;
            if bitList(x) == 1
                correctList(loop,1) = correctList(loop,1)*1;
            else
                correctList(loop,1) = correctList(loop,1)*0;
            end
        end
        bitListSum(loop,1) = sum(bitList);
    end   
end


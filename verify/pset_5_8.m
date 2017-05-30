
function output = pset_5_8()
n = 1000000;
x = zeros(n,1);
for i = 1:n
    
    x(i,1) = recurse();
end

output.m = mean(x);
output.v = mean(x.^2) - (mean(x))^2;

end


function output = recurse()
    x = ceil(rand()*3);
    if x == 1
        output = 3;
    elseif x == 2
        output = recurse() + 5;
    else
        output = recurse() + 7;
    end


end


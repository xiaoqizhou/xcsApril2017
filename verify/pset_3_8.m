
index = 0;
for i = -1:0.001:1
    index = index+ 1;
    f(index) = (3/14*(3-2*i^2))*0.001;
    e(index) = f(index)*i;
end

sum(f)
sum(f(1:1300))
sum(e)/2001

p = [0.1,0.2,0.35,0.30,0.05];
m = [0,    1,   5,  10,  20];
n = 100000;
output_m = zeros(n,1);
for i  = 1:n
    select_num = rand();
    index = 0;
    while(select_num >0)
        index = index + 1;
        select_num = select_num - p(index);
    end
    output_m(i,1) = m(index);
    
    
end

m_e = mean(output_m);
m_e2 = mean(output_m.^2);
m_var = m_e2 - (m_e)^2;

[mu,sigma,muci,sigmaci] = normfit(output_m);

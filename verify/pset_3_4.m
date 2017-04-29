output = 0;
for i = 0:4
    output = output + factorial(12)/(factorial(12-i)*factorial(i))*0.9^i*0.1^(12-i)
end
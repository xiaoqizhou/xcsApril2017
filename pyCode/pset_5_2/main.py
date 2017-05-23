import numpy
import matplotlib.pyplot as plt
loop_n = 100000
s_sum = numpy.zeros(loop_n)
cat_1 = 0
cat_2 = 0
cat_3 = 0
for i in range(0,loop_n):
    s = numpy.random.uniform(0,1,100)
    s_sum[i] = numpy.sum(s)
    if 35 <= s_sum[i] <= 40:
        cat_1 = cat_1 + 1
    elif 40 <= s_sum[i] <= 45:
        cat_2 = cat_2 + 1
    elif 60 <= s_sum[i] <= 65:
        cat_3 = cat_3 + 1

print("Sum in range (35, 40) = %f"%(float(cat_1)/loop_n))
print("Sum in range (40, 45) = %f"%(float(cat_2)/loop_n))
print("Sum in range (60, 65) = %f"%(float(cat_3)/loop_n))
print(s_sum)
count, bins, ignored = plt.hist(s_sum, 20)
plt.plot()
plt.title("X distribution")
plt.xlabel("X")
plt.ylabel("Counts")
plt.show()


s_sum_e = numpy.mean(s_sum)
s_sum_var = numpy.var(s_sum)
print("Sum mean = %f"%(s_sum_e))
print("Sum var = %f"%(s_sum_var))



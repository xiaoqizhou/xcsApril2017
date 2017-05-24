import csv
import numpy
import matplotlib.pyplot as plt
grade = []
with open("peerGrades.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        grade.append(float(row[0]))
grade_array = numpy.array(grade)
grade_mean = numpy.mean(grade_array)
print("grade mean: %f"%(grade_mean))

n = 100000 #repeat 100000 loops
grade_mean_array = numpy.zeros(n)
index = [0]*5
for i in range(0,n):
    for j in range(0,5):
        index[j] = int(numpy.floor(numpy.random.rand()*10000))  #Generate 5 random index for each grades
    grade_mean_array[i] = numpy.mean(grade_array[index]) #Get mean of the 5 grades

grade_mean_expectation = numpy.mean(grade_mean_array) #Calculate the expectation of all the mean values

grade_mean_s = float(0)
for i in range(0, len(grade_mean_array)):
    grade_mean_s = grade_mean_s \
                   + ((grade_mean_array[i] - grade_mean_expectation)**2)\
                     /(len(grade_mean_array)-1) #Calculate S^2


print("grade mean expectation: %f"%(grade_mean_expectation))
print("grade mean variance: %f"%(grade_mean_s))

count, bins, ignored = plt.hist(grade_mean_array, 20)
plt.plot()
plt.title("5 grade mean distribution")
plt.xlabel("5 grade mean")
plt.ylabel("Counts")
plt.show()

n = 100000 #repeat 100000 loops
grade_median_array = numpy.zeros(n)
index = [0]*5
for i in range(0,n):
    for j in range(0,5):
        # Generate 5 random index for each grades
        index[j] = int(numpy.floor(numpy.random.rand()*10000))
    # Get median of the 5 grades
    grade_median_array[i] = numpy.median(grade_array[index])
#Calculate the expectation of all the median values
grade_median_expectation = numpy.mean(grade_median_array)

grade_median_s = float(0)
for i in range(0, len(grade_median_array)):
    grade_median_s = grade_median_s \
                   + ((grade_median_array[i] - grade_median_expectation)**2)\
                     /(len(grade_median_array)-1) #Calculate S^2


print("grade mean expectation: %f"%(grade_median_expectation))
print("grade mean variance: %f"%(grade_median_s))

count, bins, ignored = plt.hist(grade_median_array, 20)
plt.plot()
plt.title("5 grade median distribution")
plt.xlabel("5 grade median")
plt.ylabel("Counts")
plt.show()
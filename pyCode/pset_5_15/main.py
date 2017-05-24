import csv
import numpy
import random

act = []
outcome = []
background = []
with open("background.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        background.append(row[1])
index = 0
with open("learningOutcomes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if background[index] == "less":
            act.append(row[1])
            outcome.append(float(row[2]))
        index = index + 1
act_array = numpy.array(act)
outcome_array = numpy.array(outcome)

total_1 = float(0)
num_1 = float(0)
total_2 = float(0)
num_2 = float(0)

list_1 = []
list_2 = []
for i in range(0,len(act_array)):
    if act_array[i] == "activity1":
        total_1 = total_1 + outcome_array[i]
        num_1 = num_1 + 1
        list_1.append(outcome_array[i])
    else:
        total_2 = total_2 + outcome_array[i]
        num_2 = num_2 + 1
        list_2.append(outcome_array[i])

array_1 = numpy.array(list_1)
array_2 = numpy.array(list_2)

mean_1 = numpy.mean(array_1)
mean_2 = numpy.mean(array_2)
diff = abs(mean_1 - mean_2)

print("Total 1 = %f"%(total_1))
print("Total 2 = %f"%(total_2))
print("Count 1 = %f"%(num_1))
print("Count 2 = %f"%(num_2))
print("Mean 1 = %f"%(mean_1))
print("Mean 2 = %f"%(mean_2))
print("Diff = %f"%(diff))
n = 100000 #repeat 100000 times bootstraping
new_diff = numpy.zeros(n)
p_num = float(0)
for i in range(0,n):
    #select same size of activity1 from uniform dataset
    new_selection_1 = numpy.array(random.sample(outcome, int(num_1)))
    #select same size of activity2 from uniform dataset
    new_selection_2 = numpy.array(random.sample(outcome, int(num_2)))
    #calculate mean of new activity1
    new_mean_1 = numpy.mean(new_selection_1)
    #calculate mean of new activity2
    new_mean_2 = numpy.mean(new_selection_2)
    new_diff[i] = abs(new_mean_1 - new_mean_2)
    #Compare the new observed difference with the pre-calculated difference
    if new_diff[i] >= diff:
        p_num = p_num + 1
#Calculate P-Value
p_value = p_num/n
print("P-Value = %f"%(p_value))




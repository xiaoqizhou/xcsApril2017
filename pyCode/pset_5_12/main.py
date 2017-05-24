import csv
import numpy
indicator = []
passenger_class = []
name = []
sex = []
age = []
siblings = []
parents = []
fare = []
with open("titanic.csv") as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        if index > 0:
            indicator.append(row[0])
            passenger_class.append(row[1])
            name.append(row[2])
            sex.append(row[3])
            age.append(float(row[4]))
            siblings.append(row[5])
            parents.append(row[6])
            fare.append(float(row[7]))
        index  = index + 1
p_total = [0]*6
p_true = [0]*6
sex_condition = ["female","female","female","male","male","male"]
class_condition = ["1","2","3","1","2","3"]
for i in range(0,len(indicator)):
    for j in range(0, len(sex_condition)):
        if sex[i] == sex_condition[j] and passenger_class[i] == class_condition[j]:
            p_total[j] = p_total[j]+1
            if indicator[i] == "1":
                p_true[j] = p_true[j]+1
p_total_array = numpy.array([float(i) for i in p_total])
p_true_array = numpy.array([float(i) for i in p_true])

p_array = p_true_array / p_total_array

print("P Total List")
print(p_total_array)
print("P True List")
print(p_true_array)
print("P List")
print(p_array)

p_total_2 = float(0)
p_true_2 = float(0)
for i in range(0,len(indicator)):
    if age[i] <= 10 and passenger_class[i] == "3":
        p_total_2= p_total_2+1
        if indicator[i] == "1":
            p_true_2= p_true_2+1
print("Total Class C children %f"%(p_total_2))
print("Survival Class C children %f"%(p_true_2))

p_total_2 = float(0)
p_true_2 = float(0)
for i in range(0,len(indicator)):
    if passenger_class[i] == "3":
        p_total_2= p_total_2+1
        if indicator[i] == "1":
            p_true_2= p_true_2+1
print("Total Class C %f"%(p_total_2))
print("Survival Class C %f"%(p_true_2))

p_total_3 = [float(0)]*3
p_num_3 = [float(0)]*3
class_condition = ["1","2","3"]
for i in range(0,len(indicator)):
    for j in range(0, len(class_condition)):
        if passenger_class[i] == class_condition[j]:
            p_num_3[j] = p_num_3[j]+1
            p_total_3[j] = p_total_3[j] + fare[i]

p_total_array_3 = numpy.array(p_total_3)
p_num_3 = numpy.array(p_num_3)
ep = p_total_array_3/p_num_3

print(ep)
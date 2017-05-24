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
            age.append(row[4])
            siblings.append(row[5])
            parents.append(row[6])
            fare.append(row[7])
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
print(indicator)
print(p_total)
print(p_true)


import numpy as np
import math
PI = 3.14159
f1 = open('personKeyTimingA.txt','r')
f2 = open('personKeyTimingB.txt','r')
fm = open('email.txt','r')

list_f1 = f1.readlines()
list_f2 = f2.readlines()
list_fm = fm.readlines()

list_f1 = [x.strip() for x in list_f1]
list_f2 = [x.strip() for x in list_f2]
list_fm = [x.strip() for x in list_fm]

list_f1 = [x.split(',') for x in list_f1]
list_f2 = [x.split(',') for x in list_f2]
list_fm = [x.split(',') for x in list_fm]
list_fm_time = [float(x[0]) for x in list_fm]

list_f1_time = [float(x[0]) for x in list_f1]
list_f1_letter = [x[1] for x in list_f1]
list_f2_time = [float(x[0]) for x in list_f2]
list_f2_letter = [x[1] for x in list_f2]
list_f1_duration = [0 for x in range(len(list_f1_time))]
list_f2_duration = [0 for x in range(len(list_f2_time))]
list_fm_duration = [0 for x in range(len(list_fm_time))]

for i in range(0, len(list_f1_time)):
    if i == 0:
        list_f1_duration[i] = list_f1_time[i]
    else:
        list_f1_duration[i] = list_f1_time[i] - list_f1_time[i-1]

for i in range(0, len(list_f2_time)):
    if i == 0:
        list_f2_duration[i] = list_f2_time[i]
    else:
        list_f2_duration[i] = list_f2_time[i] - list_f2_time[i-1]

for i in range(0, len(list_fm_time)):
    if i == 0:
        list_fm_duration[i] = list_fm_time[i]
    else:
        list_fm_duration[i] = list_fm_time[i] - list_fm_time[i-1]

list_f1_duration2 = [x*x for x in list_f1_duration]
list_f2_duration2 = [x*x for x in list_f2_duration]

print list_fm_duration
ex = np.mean(list_f1_duration)
ey = np.mean(list_f2_duration)

ex2 = np.mean(list_f1_duration2)
ey2 = np.mean(list_f2_duration2)
ee = np.mean(list_fm_duration)
print 'E[X] = {}'.format(ex)
print 'E[Y] = {}'.format(ey)
print 'E[X^2] = {}'.format(ex2)
print 'E[Y^2] = {}'.format(ey2)
print 'Var(X) = {}'.format(ex2 - ex**2)
print 'Var(Y) = {}'.format(ey2 - ey**2)
ex3 = ex2 - ex*ex
ey3 = ey2 - ey*ey


pai = [0 for x in range(len(list_fm_time))]
pbi = [0 for x in range(len(list_fm_time))]
for i in range(0,len(list_fm_duration)):
    x = list_fm_duration[i]
    pai[i] = math.log(1/((2*PI*ex3))) - ((x - ex)**2)/(2*ex3)
    pbi[i] = math.log(1/((2*PI*ey3))) - ((x - ey)**2)/(2*ey3)

pa = np.sum(pai)
print pa
print pai
pb = np.sum(pbi)
print pb
print pbi

p = pa - pb
print p
p2 = np.exp(p)
print p2
print ee

















f1.close()
f2.close()
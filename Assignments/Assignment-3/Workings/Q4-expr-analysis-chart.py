from timeit import default_timer
import matplotlib.pyplot as plt
import random as rn

def average1(S):
    n = len(S)
    my_average = [0]*n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        my_average[j] = total / (j+1)
    return my_average

def average2(S):
    n = len(S)
    my_average= [0]*n
    for j in range(n):
        my_average[j] = sum(S[0:j+1]) / (j+1)
    return my_average

def average3(S):
    n = len(S)
    my_average = [0]*n
    total = 0
    for j in range(n):
        total += S[j]
        my_average[j] = total / (j+1)
    return my_average

n=[10,100,1000,10000]
start = default_timer()
final_time1=[]
final_time2=[]
final_time3=[]
for i in n:
    S = [rn.randint(1,10) for _ in range(i)]
    avg1 = average1(S)
    final_time1.append(default_timer()-start)
    avg2 = average2(S)
    final_time2.append(default_timer()-start)
    avg3 = average3(S)
    final_time3.append(default_timer()-start)
 
plt.loglog(n,final_time1, label = "average1")
plt.loglog(n,final_time2, label = "average2")
plt.loglog(n,final_time3, label = "average3")
plt.legend()
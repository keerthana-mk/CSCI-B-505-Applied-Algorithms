import random
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(50000)
def algorithm1(S):
    # print("length=",type(S))
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True

def algorithm2(S):
#S:sequence
    S = sorted(S)
    for j in range(1, len(S)):
        if S[j-1] == S[j]:
            return False
    return True

def algorithm3(S, start, stop):
#slice S[start:stop],
#S:sequence
    if stop - start <= 1: return True
    elif not algorithm3(S, start, stop-1): return False
    elif not algorithm3(S, start+1, stop): return False
    else: return S[start] != S[stop-1]

def generate_sequence(input_size):
    # input_size=10
    input_list=list(random.sample(range(0,input_size),input_size))
    # print("input_list=",input_list)
    random.shuffle(input_list)
    # print("shuffled list=",input_list)
    # print("length =",len(input_list))
    return input_list

def call_algorithm1(step_size):
    input_size=10000
    input_size_list=[]
    total_time_list=[]
    while True:
        input_list=generate_sequence(input_size)
        start_time=time.time()
        output=algorithm1(input_list)
        end_time=time.time()
        input_size_list.append(input_size)
        total_time_list.append(end_time-start_time)
        if((end_time-start_time)>=45):
            break
        else:
            input_size=input_size+step_size
        print("input sizeof 1",input_size)
    print("algorithm1 run completed")
    plt.title("Algorithm 1 - Input size vs Running time")
    plt.xlabel("Input size")
    plt.ylabel("Running Time")
    plt.plot(input_size_list,total_time_list)
    plt.axhline(y=45)
    return (input_size,end_time-start_time)

def call_algorithm2(step_size):
    input_size=1000
    input_size_list=[]
    total_time_list=[]
    while True:
        input_list=generate_sequence(input_size)
        start_time=time.time()
        output=algorithm2(input_list)
        end_time=time.time()
        input_size_list.append(input_size)
        total_time_list.append(end_time-start_time)
        if((end_time-start_time)>=45):
            break
        else:
            input_size=input_size+step_size
        print("input sizeof 2",input_size)
    print("algorithm2 run completed")
    plt.title("Algorithm 2 - Input size vs Running time")
    plt.xlabel("Input size")
    plt.ylabel("Running Time")
    plt.plot(input_size_list,total_time_list)
    plt.axhline(y=45)
    return (input_size,end_time-start_time)

def call_algorithm3(step_size):
    input_size=10
    input_size_list=[]
    total_time_list=[]
    while True:
        input_list=generate_sequence(input_size)
        print("input_size: {}".format(input_size))
        start_time=time.time()
        output=algorithm3(input_list,0,len(input_list))
        end_time=time.time()
        input_size_list.append(input_size)
        total_time_list.append(end_time-start_time)
        print("input sizeof 3",input_size,(end_time-start_time))
        if((end_time-start_time)>=45):
            break
        else:
            input_size=input_size+step_size
    print("algorithm3 run completed")
    plt.title("Algorithm 3 - Input size vs Running time")
    plt.xlabel("Input size")
    plt.ylabel("Running Time")
    plt.plot(input_size_list,total_time_list)
    plt.axhline(y=45)
    return (input_size,end_time-start_time)


    step_size1,time1=call_algorithm1(5000)
    step_size2,time2=call_algorithm2(10000000)
    step_size3,time3=call_algorithm3(2)

    print("===========Algorithm 1===========")
    print("Algorithm1 with input size ={}, runs in {} secs" .format(step_size1,time1))
    print("===========Algorithm 2===========")
    print("Algorithm2 with input size ={}, runs in {} secs".format(step_size2,time2))
    print("===========Algorithm 3===========")
    print("Algorithm3 with input size ={}, runs in {} secs".format(step_size3,time3))
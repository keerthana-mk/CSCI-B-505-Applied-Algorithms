import matplotlib.pyplot

def average1(S):
    #S:sequence
    n = len(S)
    my_average = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
            my_average[j] = total / (j+1)
    return my_average

def average2(S):
    #S:sequence
    n = len(S)
    my_average= [0] * n
    for j in range(n):
         my_average[j] = sum(S[0:j+1]) / (j+1)
    return my_average

def average3(S):
    #S:sequence
    n = len(S)
    my_average = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        my_average[j] = total / (j+1)
    return my_average

if __name__=='__main__':
    print("=============Algorithm1============")

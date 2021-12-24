import random

def counting_Sort(inputA, outputB, k):
    input_length = len(inputA)
    Freq_list = [0 for i in range(0, k + 1)]
    for j in range(0, input_length):
        Freq_list[inputA[j]] = Freq_list[inputA[j]] + 1
    for i in range(1, k + 1):
        Freq_list[i] = Freq_list[i] + Freq_list[i - 1]
    for m in range(input_length - 1, -1, -1):
        outputB[Freq_list[inputA[m]] - 1] = inputA[m]
        Freq_list[inputA[m]] = Freq_list[inputA[m]] - 1
    return outputB


ListA = [1, 2, 2, 3, 4, 4, 5]
random.shuffle(ListA)
ListB = [0 for i in range(len(ListA))]
k = max(ListA)
counting_Sort(ListA, ListB, k)

def parent(i):
    return i // 2


# Since using 0 based index
def left_child(i):
    return (2 * (i + 1)) - 1


# Since using 0 based index
def right_child(i):
    return 2 * (i + 1)


def max_heapify(ListA, i, heap_size):
    left = left_child(i)
    right = right_child(i)
    if left <= heap_size and ListA[left] > ListA[i]:
        largest = left
    else:
        largest = i
    if right <= heap_size and ListA[right] > ListA[largest]:
        largest = right
    if largest != i:
        # print("before swap : ", ListA)
        ListA[i], ListA[largest] = ListA[largest], ListA[i]
        # print("swap happened? : ", ListA)
        max_heapify(ListA, largest, heap_size)


def build_max_heap(ListA):
    A_heapsize = len(ListA) - 1
    for i in range(A_heapsize // 2, -1, -1):
        max_heapify(ListA, i, A_heapsize)


def heapsort(ListA):
    build_max_heap(ListA)
    # print("after building max heap: ", ListA)
    n = len(ListA) - 1
    for i in range(len(ListA) - 1, 0, -1):
        ListA[0], ListA[i] = ListA[i], ListA[0]
        n = n - 1
        max_heapify(ListA, 0, n)
    print(ListA)


A = [11, -2, 7, 3, 6, 8, -10, 3, 11]
heapsort(A)

# n = len(A)
# # for i in range(0, n):
# #     print("%d" % (A[n:0:-1])),

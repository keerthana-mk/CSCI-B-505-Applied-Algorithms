from collections import deque
class Solution(object):
    ##Bottom-Up Solution
      def sortArray(self,nums):
        ##First, break list into a list of lists e.g [[1],[4], ...]    
        l = [[num] for num in nums]
        ##Second, store lists in queue.
        queue = deque(l)
        ##Define merge method, I took the same merge method from the Top-Down algo example provided. 
        def merge(left_list, right_list):
            left_cursor = right_cursor = 0
            ret = []
            while left_cursor < len(left_list) and right_cursor < len(right_list):
                if left_list[left_cursor] < right_list[right_cursor]:
                    ret.append(left_list[left_cursor])
                    left_cursor += 1
                else:
                    ret.append(right_list[right_cursor])
                    right_cursor += 1

        # append what is remained in either of the lists
            ret.extend(left_list[left_cursor:])
            ret.extend(right_list[right_cursor:])
            print(ret)
            return ret
        ##Merge Sort Bottom-up method starts here.
        while(len(queue) > 1):  
        #Pop left and right lists from queue
            left_list = queue.popleft()
            right_list = queue.popleft()
        #Merge lists until there is one list left in the queue
            queue.append(merge(left_list,right_list))
        #Pop last remaining sorted list
        return queue.pop() 

m=Solution()
m.sortArray([1,4,2,56,45,6])

def mergesort(ListS):
    S_length = len(ListS)
    
   #checking base case if queue has 0 or 1 elements it is already sorted
    if S_length <= 1:
        return    
    # auxilary queue to store the left and right part after dividing by mid
    ListA = []
    ListB = []
    
    #add left part till mid of original queue  to ListA
    while len(ListA) < S_length//2:
        ListA.append(ListS.pop(0))

    #add right part from mid of original queue  to ListB
    while len(ListS) > 0:
        ListB.append(ListS.pop(0))
#   call merge sort on ListA to sort the elements in that queue.
    mergesort(ListA)
#   call merge sort on ListB to sort the elements in that queue.
    mergesort(ListB)
#     merge Sorted ListA and ListB
    merge(ListA, ListB, ListS)

    
    
def merge(ListA, ListB, ListS):
   #checking ListA and ListB are not empty
    while len(ListA) > 0 and len(ListB) > 0:
#         Compare the elements of ListA and ListB and append to ListS
        if ListA[0] < ListB[0]:
            ListS.append(ListA.pop(0))
        else:
            ListS.append(ListB.pop(0))
    # add remaining elements of ListA to queue ListS
    while len(ListA) > 0:
        ListS.append(ListA.pop(0))
    
    # add remaining elements of ListB to queue ListS
    while len(ListB) > 0:
        ListS.append(ListB.pop(0))
    
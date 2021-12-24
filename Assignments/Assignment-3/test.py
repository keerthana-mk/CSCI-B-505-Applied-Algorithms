from functools import reduce
list2 =[1,2,3,4,5]
fins = reduce(lambda x,y:x+y, list2)
print(fins)
import argparse
from functools import reduce

#initialise argument parser
parser = argparse.ArgumentParser()
# #add an argument to parse list of numbers
# -lst => argument_option for specifying a list
# nargs => '+' is the Regular expression to accept 1 or more characters of list
# default => [optional] specifies a default Value
# help => display the description if help option is given
parser.add_argument('-lst', nargs='+', default = ['1'], help="List of numbers")
args = parser.parse_args()

#Function to compute sum of numbers in a given list
def sum_of_numbers(listA):
    sum=0
    for i in listA:
        sum=sum+i
    return sum

#Function to generate reciprocal of the numbers in the given list and call sum_of numbers function to compute sum of reciprocals.
def sum_of_reciprocal(N):
    sum=0
    if len(N)>0:
        #using lambda function to convert numbers in list to reciprocals
        sum=sum_of_numbers(list(map(lambda x:(1/int(x)),N)))
        print("Sum of reciprocals of list {} is {}".format(N,sum))

if __name__=='__main__':
    sum_of_reciprocal(args.lst)




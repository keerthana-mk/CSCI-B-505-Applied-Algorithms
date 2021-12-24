# ## Problem 2: Console I/O -argparse module
# https://docs.python.org/3/howto/argparse.html

# In[45]:


import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-lst',nargs='+',default=['1'], help="List of numbers")
parser.add_argument('-op', default = 'sum', help = "sum, prod, rec")
args=parser.parse_args()
print(args.lst)
print(args.op)


import argparse


def f(*x,**y):
    def s1(x):
        s=0
        if x:
            for i in x:
                s+=i
        return s
    
    def p1(x):
        p=1
        if x:
            for i in x:
                p*=i
        return p

    
    # def sum_of_reciprocal(x):
    #     s=0
    #     if x:
    #         for i in x:
    #             s=s+(1/i)
    #     return s



    if y["action"]=="sum":
        return s1(*x)
    elif y["action"]=="product":
        return p1(*x)
    # elif y["action"]=="reciprocal":
    #     return sum_of_reciprocal(*x)
    else:
        return f"bad argument: {y}"

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-lst', nargs='*', default = [],type=int, help="List of numbers")
    parser.add_argument('-op' ,default='sum', help="sum prod etc")
    args=parser.parse_args()
    A=args.lst

    # print(A)
   # A=[1,2,3,4]
    print("{} of number in list ={}".format(args.op,f(A, action=args.op)))
    # print(Func_sum_prod(A, action="product"))
    # print(Func_sum_prod(A, action="reciprocal"))
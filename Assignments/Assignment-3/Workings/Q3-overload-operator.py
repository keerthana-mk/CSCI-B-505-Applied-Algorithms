import time

class complex_:
    def __init__(self, re=0,im=0):
        self.re=re
        self.im=im
        
    def get_re(self):
        return self.re
    
    def get_im(self):
        return self.im
    
    def __str__(self):
        g=lambda x:"+" if x>=0 else ""
        return f"({self.re}{g(self.im)}{self.im}i)" 
    
    def cadd(self, other):
        new_re=self.get_re()+other.get_re()
        new_im=self.get_im()+other.get_im()
        return complex_(new_re,new_im)
    
    def __add__(self,other):
        new_re= self.get_re()+other.get_re()
        new_im=self.get_im()+other.get_im()
        return complex_(new_re,new_im)

    def cmul(self,other):
        new_re = ((self.get_re()*other.get_re())-(self.get_im()*other.get_im()))
        new_im = ((self.get_re()*other.get_im())+(self.get_im()*other.get_re()))
        return complex_(new_re,new_im)
#  multiplication of complex numbers (a+bi)(c+di)=(ac-bd)+(ad+bc)i
#  overiding * operator
    def __mul__(self,other):
        new_re = ((self.get_re()*other.get_re())-(self.get_im()*other.get_im()))
        new_im = ((self.get_re()*other.get_im())+(self.get_im()*other.get_re()))
        return complex_(new_re,new_im)

if __name__=='__main__':
    start_time=time.time()
    w=complex_(1,-3)
    x = complex_(-1,3)
    y = complex_(1,3)
    z = complex_(-1,-3)
    
    print("w=",w)
    print("x=",x)
    print("y=",y)
    print("z=",z)
    
    #using function overload
    print("add(w,x,y,z)=",w.cadd(x).cadd(y).cadd(z))
    print("product(x,y,z)=",x.cmul(y).cmul(z))

    #operator overloading
    print("sum=", w+z)
    print("mul=",x*y*z)
    # print("total runtime=",round(float(time.time()-start_time),5))
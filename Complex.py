import math

class Complex(object):

    def __init__(self,a,b):
        '''creates complex Number'''
        self.a=a
        self.b=b
    
    def __str__(self):
        c=str(self.a)+' + '+str(self.b)+'i'
        return c
         

    def add(self,rhs):
        '''Adds complex numbers'''
        new_a=self.a+rhs.a
        new_b=self.b+rhs.b
        return Complex(new_a,new_b)

    def sub(self,rhs):
        '''Subtract complex number'''
        new_a=self.a-rhs.a
        new_b=self.b-rhs.b
        return Complex(new_a,new_b)

    def mul(self,rhs):
        '''Multiply complex no'''
        new_a=self.a*rhs.a-self.b*rhs.b
        new_b=self.a*rhs.b+self.b*rhs.a
        return Complex(new_a,new_b)

    def div(self,rhs):
        '''Divide two numbers'''
        try:
            new_a=(self.a*rhs.a-self.b*rhs.b)/(  (rhs.a)**2+(rhs.b)**2  )
            new_b=(self.a*rhs.b+self.b*rhs.a)/(  (rhs.a)**2+(rhs.b)**2 )
            return Complex(new_a,new_b)
        except ZeroDivisionError:
            print ('dont take equal imag and real part in second number')

    def real(self):
        return self.a

    def imag(self):
        return self.b

    def conjugate(self):
        return Complex(self.a,-self.b)

    def absolute(self):
        return math.sqrt( (self.a)**2+(self.b)**2 ) 

    def argument(self):
        '''Find argument'''
        try:
            a=math.atan(self.a/self.b)
            return a
        except ZeroDivisionError:
            print 'imaginary part should not be zero'

    



x=Complex(9,2)
y=Complex(8,-6)
print x
print y

z=x.add(y)
#print z

m=x.sub(y)
#print m

s=x.mul(y)
#print s

z=x.div(y)
#print z

z=x.conjugate()
#print z

z=x.absolute()
#print z

z=x.argument()
#print z





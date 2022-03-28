from sympy import*
import numpy as np
import math
epl=0.4

x1=symbols('x1')
x2=symbols('x2')
f=(x1-2)**2+(x1-2*x2)**2

endx1=0
endx2=3
alpha=0.000000

def xunhuan(endx1,endx2,alpha,epl):###d是方向，gra是梯度 endx是答案
    x1=symbols('x1')
    x2=symbols('x2')
    f=(x1-2)**2+(x1-2*x2)**2
    d1=-1*diff(f,x1)
    d1=d1.evalf(subs={x1:endx1,x2:endx2})
    d2=-1*diff(f,x2)
    d2=d2.evalf(subs={x1:endx1,x2:endx2})
    gra1=diff(f,x1)
    gra1=gra1.evalf(subs={x1:endx1,x2:endx2})
    gra2=diff(f,x2)
    gra2=gra2.evalf(subs={x1:endx1,x2:endx2})
    if(sqrt(gra1**2+gra2**2)<=epl):
        alpha1=symbols('alpha')
        x1=endx1+alpha1*d1
        x2=endx2+alpha1*d2
        f1=(x1-2)**2+(x1-2*x2)**2
        f1=diff(f1,alpha1)
        alpha=solve(f1,alpha1)

        aa=alpha[0]

        #endx1=endx1+aa*d1
        #endx2=endx2+aa*d2
        print(endx1)
        print(endx2)
    else:
        alpha1=symbols('alpha')
        x1=endx1+alpha1*d1
        x2=endx2+alpha1*d2
        f1 = (x1 - 2) ** 2 + (x1 - 2 * x2) ** 2
        f1=diff(f1,alpha1)

        alpha=solve(f1,alpha1)

        aa = alpha[0]
        endx1=endx1+aa*d1
        endx2=endx2+aa*d2
        xunhuan(endx1,endx2,alpha,epl)
        
        
xunhuan(endx1,endx2,alpha,epl)

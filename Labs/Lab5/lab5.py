# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: (np.e)**(x**2+7*x-30)
    fp = lambda x: (2*x+7)*(np.e)**(x**2+7*x-30)
    fpp = lambda x: 2*(np.e)**(x**2+7*x-30) + ((2*x+7)**2)*(np.e)**(x**2+7*x-30)
    a = 2
    b = 4.5

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1
    Nmax = 100
    tol = 1e-7

    [astar,ier] = bisection(f,fp,fpp,a,b)
    if (ier == 0): [p,pstar,info,it] = newton(f,fp,astar,tol,Nmax)
    if (ier != 0): print('ERROR: bisection error is:',ier)
    elif (info != 0): print('ERROR: newton error is:',info)
    print('the approximate root is',pstar)




# define routines
def bisection(f,fp,fpp,a,b):
    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb == 0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs((f(d)*fpp(d))/(fp(d)**2)) >= 1):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
    
    astar = d
    ier = 0
    return [astar, ier]
  
def newton(f,fp,p0,tol,Nmax): 
    p = np.zeros(Nmax+1);
    p[0] = p0
    for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
        pstar = p1
        info = 0
        return [p,pstar,info,it]
      p0 = p1
    pstar = p1
    info = 1
    return [p,pstar,info,it]  
      
driver()               
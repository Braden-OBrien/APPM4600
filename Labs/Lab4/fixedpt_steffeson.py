# import libraries
import numpy as np
    
# define routines
def fixedpt(f,pn,tol,Nmax):

    ''' pn = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    a = pn
    b = f(pn)
    c = f(b)

    x0 = a

    out_arr = np.array([[x0]]) #insert initial guess of x0

    count = 0
    while (count < Nmax):
       count = count +1
       x1 = a - ((b-a)**2)/(c-2*b+a)
       out_arr = np.append(out_arr, [[x1]], axis=0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier,out_arr]
       x0 = x1
       a = x0
       b = f(x0)
       c = f(b)

    xstar = x1
    ier = 1
    return [xstar,ier,out_arr]
    

# use routines 
f1 = lambda x: (10/(x+4))**(1/2)
''' 
fixed point is alpha1 = 1.4987....
'''

Nmax = 100
tol = 1e-10

''' test f1 '''
pn = 1.5
[xstar,ier,out_arr] = fixedpt(f1,pn,tol,Nmax)
print('the approximate fixed point is:',xstar)
print('f1(xstar):',f1(xstar))
print('Error message reads:',ier)
print('Array of iteration values:\n',out_arr)

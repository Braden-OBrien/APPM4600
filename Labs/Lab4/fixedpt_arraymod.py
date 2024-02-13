# import libraries
import numpy as np
    
# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    out_arr = np.array([[x0]]) #insert initial guess of x0

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       out_arr = np.append(out_arr, [[x1]], axis=0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier,out_arr]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar,ier,out_arr]
    

# use routines 
f1 = lambda x: 1+0.5*np.sin(x)
''' 
fixed point is alpha1 = 1.4987....
'''

Nmax = 100
tol = 1e-6

''' test f1 '''
x0 = 0.0
[xstar,ier,out_arr] = fixedpt(f1,x0,tol,Nmax)
print('the approximate fixed point is:',xstar)
print('f1(xstar):',f1(xstar))
print('Error message reads:',ier)
print('Array of iteration values:\n',out_arr)

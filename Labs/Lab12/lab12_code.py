import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time


def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     """for N in [100, 500, 1000, 2000, 4000, 5000]:
          ''' Right hand side'''
          b = np.random.rand(N,1)
          A = np.random.rand(N,N)
          
          print("N =",N)
          
          start_time = time.perf_counter() 
          x = scila.solve(A,b)
          tot_time  = time.perf_counter()-start_time
          test = np.matmul(A,x)
          r = la.norm(test-b)
          
          print('from reduction:', r)
          print('CPU total time is:', tot_time)
          
          start_time = time.perf_counter()
          lu_factor = scila.lu_factor(A)
          mid_time = time.perf_counter()
          y = scila.lu_solve(lu_factor, b)
          tot_time = time.perf_counter()
          test = np.matmul(A, y)
          r = la.norm(test-b)
          
          print('from lu factorization:', r)
          print('LU factor time is:', mid_time-start_time)
          print('LU solve time is:', tot_time-mid_time)"""

     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)
     
     '''Normal equation solve'''
     start_time = time.perf_counter()
     T = np.transpose(A)
     pt1 = np.matmul(T, A)
     pt2 = np.matmul(T, b)
     sol = la.solve(pt1, pt2)
     tot_time = time.perf_counter()-start_time
     test = np.matmul(A, sol)
     r = la.norm(test-b)
     print('for normal equation solve:', r)
     print('CPU time is:', tot_time)
     
     start_time = time.perf_counter()
     Q, pt1= la.qr(A)
     pt2 = np.matmul(Q.T, b)
     sol = la.solve(pt1, pt2)
     tot_time = time.perf_counter()-start_time
     test = np.matmul(A, sol)
     r = la.norm(test-b)
     print('for qr factorization solve:', r)
     print('CPU time is:', tot_time)
     




     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B
          
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       

import numpy as np #using numpy for arithmetic
import matplotlib.pyplot as plt #using pyplot for plotting purposes

x = np.arange(1.920, 2.080, 0.001) #setting domain

Y_poly = np.power(x, 9) - 18*np.power(x, 8) + 144*np.power(x, 7) - 672*np.power(x, 6) + 2016*np.power(x, 5) - 4032*np.power(x, 4) + 5376*np.power(x, 3) - 4608*np.power(x, 2) + 2304*x - 512 #equation polynomial form

Y_exp = np.power((x-2), 9) #equation binomial form

plt.plot(x, Y_poly)

plt.savefig("p1-Y_poly") #saving figures

plt.clf()

plt.plot(x, Y_exp)

plt.savefig("p1-Y_exp")


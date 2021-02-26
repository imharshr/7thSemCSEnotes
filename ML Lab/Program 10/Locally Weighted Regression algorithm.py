#!/usr/bin/env python
# coding: utf-8

# # Example 1: Fitting to Give n Ploynomial Of degree 1 (Linear Regression)

# In[8]:


from math import ceil
import numpy as np
from scipy import linalg  
 
 
def lowess(x, y, f= 2. / 3., iter=3):
    
    n = len(x) # Number of x  points 
    print("N :", n)
    r = int(ceil(f * n))  # Computing the residual of smoothing functions
    print("R : ",r)
    #print("np.abs(x - x[i]) : ",np.sort(np.abs(x - x[56]))[r])
    h = [np.sort(np.abs(x - x[i]))[r] for i in range(n)] #
    #print("H : ", h)
    #print("np.abs((x[:, None] - x[None, :]) / h) : ",np.abs((x[:, None] - x[None, :]) / h))
    w = np.clip(np.abs((x[:, None] - x[None, :]) / h), 0.0, 1.0)  # Weight Function 
    #print("W : ", w)
    w = (1 - w ** 3) ** 3  # Tricube Weight Function
    #print("W After : ", w)
    ypred = np.zeros(n) # Initialisation of predictor 
    #print("Y pred : ", ypred)
    delta = np.ones(n)  # Initialisation of delta
    #print("Delta : ", delta)
   
    for iteration in range(iter):
        for i in range(n):
            weights = delta * w[:, i] # Cumulative Weights 
            #print("Weights : ", weights)
            b = np.array([np.sum(weights * y), np.sum(weights * y * x)]) # Matrix B
            A = np.array([[np.sum(weights), np.sum(weights * x)],
                          [np.sum(weights * x), np.sum(weights * x * x)]]) # Matrix A
                      
            beta = linalg.solve(A, b) # Beta,Solution of AX= B equation 
            ypred[i] = beta[0] + beta[1] * x[i]
             
        residuals = y - ypred   # Finding Residuals
        s = np.median(np.abs(residuals))  # Median of Residuals
        delta = np.clip(residuals / (6.0 * s), -1, 1)  # Delta
        delta = (1 - delta ** 2) ** 2   # Delta 
 
    return ypred

if __name__ == '__main__':  # Main Function
    
    import math
    
    n = 100  # Number of data points
   
    #Case1: Sinusoidal Fitting 
    x = np.linspace(0, 2 * math.pi, n)
    print(x.shape)
    y = np.sin(x) + 0.3 * np.random.randn(n) 
    print("Y : ", y.shape)
    
    #Case2 : Straight Line Fitting
    #x=np.linspace(0,2.5,n) # For Linear
    #y= 1 + 0.25*np.random.randn(n) # For Linear
    
    f = 0.25
    ypred = lowess(x, y, f=f, iter=3)
    
    import pylab as pl
    pl.clf()
    pl.plot(x, y, label='Y NOISY')
    pl.plot(x, ypred, label='Y PREDICTED')
    pl.legend()
    pl.show()


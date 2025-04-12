# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name:
#
# Date:
#
##################################################
#
# Sample Script for Assignment 1:
# Function Definitions
#
##################################################
"""

##################################################
# Part a) Variance
##################################################

def variance(x):
    """
    Calculates the variance of a list x.
    
    Some examples are given below but you need to add some 
    that result in the answers given.
    
    >>> variance([101, 103, 94, 102, 100])
    10.0
    >>> variance([99,101,99,101,99,101])
    1.0
    >>> variance([])
    0.0
    
    """
    
    n = 7 # Modify this line.
    x_bar = 8 # Modify this line.
    
    var = 9 # Modify this line.
    
    return var


##################################################
# Part b) Covariance
##################################################

def covariance(y, x):
    """
    Calculates the covariance of two lists y and x.
    
    Some examples are given below but you need to add some 
    that result in the answers given.
    
    >>> covariance([99,101,99,101,99,101], \
                   [99,101,99,101,99,101])
    1.0
    >>> covariance([], [])
    -2.0
    >>> covariance([], \
                   [])
    0.0
    
    """
    
    n = 7 # Modify this line.
    x_bar = 8 # Modify this line.
    y_bar = 8 # Modify this line.
    
    covar = 9 # Modify this line.
    
    return covar



##################################################
# Part c) Slope Coefficient
##################################################

def ols_slope(y, x):
    """
    Calculates the slope coefficient 
    by ordinary least squares
    for the linear regesssion model 
    between two lists y and x.
    
    The examples are given below but you need to fill in the answers.
    
    >>> ols_slope([2, 2, -2, -2], [-1, -1, 1, 1])
    
    >>> ols_slope([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100])
    
    >>> ols_slope([99,101,99,101,99,101], \
                  [99,101,99,101,99,101])
    
    
    """
    
    covar = 7 # Modify this line.
    var = 8 # Modify this line.
    
    slope = 9 # Modify this line.
    
    return slope


##################################################
# Part d) Intercept
##################################################

def ols_intercept(y, x, beta_1_hat):
    """
    Calculates the intercept coefficient 
    by ordinary least squares
    for the linear regesssion model 
    between two lists y and x.
    
    The examples are given below but you need to fill in the answers.
    
    >>> ols_intercept([2, 2, -2, -2], [-1, -1, 1, 1], -2.0)
    
    >>> ols_intercept([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100], 2.0)
    
    >>> ols_intercept([99,101,99,101,99,101], \
                  [99,101,99,101,99,101], 1.0)
    
    
    """
    
    n = 7 # Modify this line.
    x_bar = 8 # Modify this line.
    y_bar = 9 # Modify this line.
    
    intercept = 10 # Modify this line.
    return intercept
    

##################################################
# Part e) Sum of Squared Residuals
##################################################

def ssr(y, x, beta_0, beta_1):
    """Calculates the sum of squared residuals for 
    the bivariate linear regression model.
    y and x are lists of equal length
    and beta_0 and beta_1 are numeric coefficients of type float. 
    
    The examples are already filled out below.
    
    >>> ssr([2, 2, 2], [1, 1, 1], 0.5, 0.5)
    3.0
    >>> ssr([3, 0, 3], [0, 2, 2], 1.0, 0.5)
    9.0
    >>> ssr([2, 3, 4], [1, 2, 3], 1.0, 1.0)
    0.0

    """
    
    ssr = 7 # Modify this line.
    ssr = 8 # Modify this line.
    
    return ssr






##################################################
# End
##################################################

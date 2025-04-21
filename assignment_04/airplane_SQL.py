# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: Kaylei Burcham
#
# Date:4/21/2025
#
##################################################
#
# Sample Script for Assignment 4:
# Obtaining Data from a Database
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import pandas as pd
import os
import sqlite3 as dbapi
import statsmodels.formula.api as sm


##################################################
# Set up Workspace
##################################################

os.chdir(os.path.dirname(os.path.realpath(__file__)))
print("Current Working Directory:", os.getcwd())


##################################################
# Question 1: Connect to a Database
#     and Obtain Sales Data
##################################################

#--------------------------------------------------
# a. Connect to the database called airplanes.db
#     and obtain a cursor object.
#--------------------------------------------------

con = dbapi.connect("airplanes.db")
cur = con.cursor()


#--------------------------------------------------
# b. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------

query_1 = """
    SELECT *
    FROM Sales
"""
print(query_1)
cur.execute(query_1)

#--------------------------------------------------
# c. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

airplane_sales = pd.DataFrame(cur.fetchall(), columns=[col[0] for col in cur.description])
print(airplane_sales.describe())
print(airplane_sales.columns)

#--------------------------------------------------
# Fit a regression model to check progress.
#--------------------------------------------------

reg_model_sales = sm.ols(formula="price ~ age", data=airplane_sales).fit()
print(reg_model_sales.summary())


##################################################
# Question 2: Obtain Specification Data
##################################################

#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the sales data joined with specification data.
#--------------------------------------------------
# Check actual columns in the three tables

query_2 = """
    SELECT s.*, sp.passengers, sp.wtop, sp.fixgear, sp.tdrag
    FROM Sales s
    JOIN Specs sp ON s.sale_id = sp.sale_id
"""

print(query_2)
cur.execute(query_2)

#--------------------------------------------------
# b. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

airplane_sales_specs = pd.DataFrame(cur.fetchall(), columns=[col[0] for col in cur.description])
print(airplane_sales_specs.describe())
print(airplane_sales_specs.columns)

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_sales_specs = sm.ols(
    formula="price ~ age + passengers + wtop + fixgear + tdrag",
    data=airplane_sales_specs
).fit()
print(reg_model_sales_specs.summary())


##################################################
# Question 3: Obtain Performance Data
##################################################

#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the sales data joined with specification data
#    and then joined with the performance data.
#--------------------------------------------------

query_3 = """
    SELECT s.*, sp.passengers, sp.wtop, sp.fixgear, sp.tdrag,
           pf.horse, pf.fuel, pf.ceiling, pf.cruise
    FROM Sales s
    JOIN Specs sp ON s.sale_id = sp.sale_id
    JOIN Perf pf ON s.sale_id = pf.sale_id
"""

print(query_3)
cur.execute(query_3)

#--------------------------------------------------
# b. Create a data frame and load the query.
#--------------------------------------------------

airplane_full = pd.DataFrame(cur.fetchall(), columns=[col[0] for col in cur.description])
print(airplane_full.describe())
print(airplane_full.columns)

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(
    formula="""
        price ~ age + passengers + wtop + fixgear + tdrag + 
        horse + fuel + ceiling + cruise
    """,
    data=airplane_full
).fit()
print(reg_model_full.summary())


##################################################
# Commit changes and close the connection
##################################################

con.close()

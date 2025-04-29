# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: [Kaylei Burcham]
#
# Date: [4/29/2025]
#
##################################################
#
# Final Examination: Data Handling and Predictive Modeling
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import sqlite3
import pandas as pd
import statsmodels.formula.api as sm
import math
import os

##################################################
# Set up Workspace
##################################################

# Set working directory to where the customers.db file is located
os.chdir(r"C:\Users\Kaylei Burcham\Desktop\2mybrainfuzzies\2mybrainfuzzies\Final Exam")
 
# Check the current working directory
print("Current Working Directory:", os.getcwd())

##################################################
# Question 1: Connect to a Database
#     and Obtain Applications Data
##################################################

#--------------------------------------------------
# a. Connect to the database called customers.db
#     and obtain a cursor object.
#--------------------------------------------------

# Connect to the database called customers.db and obtain a cursor object
con = sqlite3.connect("customers.db")
cur = con.cursor()


#--------------------------------------------------
# b. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------

query_1 = """
SELECT income, homeownership, purchases, credit_limit
FROM Applications
"""
print(query_1)
cur.execute(query_1)

#--------------------------------------------------
# c. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

purchase_app = pd.DataFrame(cur.fetchall(), columns=[i[0] for i in cur.description])

# Describe the contents of the dataframe to check the result.

purchase_app.describe()
purchase_app.columns
print(purchase_app.describe())
print(purchase_app.columns)

#--------------------------------------------------
# Fit a regression model to check progress.
#--------------------------------------------------

reg_model_app = sm.ols(
    formula="purchases ~ income + homeownership + credit_limit",
    data=purchase_app
).fit()

# Display a summary table of regression results.
print(reg_model_app.summary())

##################################################
# Question 2: Obtain CreditBureau Data
##################################################

#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the Application data joined with CreditBureau data.
#--------------------------------------------------

query_2 = """
    SELECT A.income, A.homeownership, A.purchases, A.credit_limit, 
           B.fico, B.num_late, B.past_def, B.num_bankruptcy
    FROM Applications A
    INNER JOIN CreditBureau B
    ON A.ssn = B.ssn
"""
print(query_2)
cur.execute(query_2)

#--------------------------------------------------
# b. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

purchase_app_bureau = pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description])

# Describe the contents of the dataframe to check the result.
print(purchase_app_bureau.describe())
print(purchase_app_bureau.columns)

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_app_bureau = sm.ols(
    formula="purchases ~ income + homeownership + credit_limit + fico + num_late + past_def + num_bankruptcy",
    data=purchase_app_bureau
).fit()

# Display a summary table of regression results.
print(reg_model_app_bureau.summary())

##################################################
# Question 3: Obtain Demographic Data
##################################################

#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the Application data joined with CreditBureau data
#    and Demographic data.
#--------------------------------------------------

query_3 = """
    SELECT A.income, A.homeownership, A.purchases, A.credit_limit, 
           B.fico, B.num_late, B.past_def, B.num_bankruptcy,
           D.avg_income, D.density
    FROM Applications A
    INNER JOIN CreditBureau B
    ON A.ssn = B.ssn
    INNER JOIN Demographic D
    ON A.zip_code = D.zip_code
"""
print(query_3)
cur.execute(query_3)

#--------------------------------------------------
# b. Create a data frame and load the query
#--------------------------------------------------

purchase_full = pd.DataFrame(cur.fetchall(), columns=[i[0] for i in cur.description])
 
purchase_full.describe()
purchase_full.columns

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(
    formula="purchases ~ income + homeownership + credit_limit + fico + num_late + past_def + num_bankruptcy + avg_income + density",
    data=purchase_full
).fit()

# Display a summary table of regression results.
print(reg_model_full.summary())

##################################################
# Question 4: Advanced Regression Modeling
##################################################

#--------------------------------------------------
# Parts a-c with utilization.
#--------------------------------------------------

# Create a variable for credit utilization.
purchase_full["utilization"] = purchase_full["purchases"] / purchase_full["credit_limit"]

# Check the new variable
print(purchase_full["utilization"].describe())

# Fit a regression model predicting utilization
reg_model_util = sm.ols(
    formula="utilization ~ income + homeownership + fico + num_late + past_def + num_bankruptcy + avg_income + density",
    data=purchase_full
).fit()

print(reg_model_util.summary())

#--------------------------------------------------
# Parts d-f with log_odds_util.
#--------------------------------------------------

# Create a variable for log odds of utilization
purchase_full["log_odds_util"] = purchase_full["utilization"].apply(
    lambda x: math.log(x / (1 - x)) if (x > 0) and (x < 1) else None
)

# Check the new variable
print(purchase_full["log_odds_util"].describe())

# Fit a regression model predicting log_odds_util
reg_model_logodds = sm.ols(
    formula="log_odds_util ~ income + homeownership + fico + num_late + past_def + num_bankruptcy + avg_income + density",
    data=purchase_full.dropna(subset=["log_odds_util"])
).fit()

print(reg_model_logodds.summary())

##################################################
# Commit changes and close the connection
##################################################

# No changes were necessary -- only reading.
con.close()

# Then we can continue with this file when you have time
# to work on it later.



##################################################
# Extra code snippets
##################################################

# In case things go wrong, you can always drop the table
# and start over:
# cur.execute('DROP TABLE Applications')
# cur.execute('DROP TABLE CreditBureau')
# cur.execute('DROP TABLE Demographic')

# This can get the schema of the table,
# cur.execute("PRAGMA table_info('Applications')").fetchall()
# cur.execute("PRAGMA table_info('CreditBureau')").fetchall()
# cur.execute("PRAGMA table_info('Demographic')").fetchall()
# which states the names of the variables and the data types.


##################################################
# End
##################################################
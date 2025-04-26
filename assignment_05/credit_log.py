# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 18:37:24 2025

@author: Kaylei Burcham
"""

# credit_logit.py
 
# NAME
# Assignment 5
 
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
 
# Style settings
sns.set(style="whitegrid", color_codes=True)
 
# Set working directory to the location of this script
os.chdir(os.path.dirname(os.path.realpath(__file__)))
 
# Load the dataset
credit = pd.read_csv('credit_data.csv')
 
# -----------------------------
# Full Model
# -----------------------------
 
# All predictors (exclude 'default')
X_full = credit.drop(columns='default')
y = credit['default']
 
# Fit logistic regression using statsmodels
X_full_sm = sm.add_constant(X_full)
logit_full_model = sm.Logit(y, X_full_sm).fit()
 
# Print summary results for README
print("\n--- FULL MODEL SUMMARY ---\n")
print(logit_full_model.summary())
 
# Fit using sklearn for ROC
logit_sk_full = LogisticRegression(max_iter=1000)
logit_sk_full.fit(X_full, y)
pred_probs_full = logit_sk_full.predict_proba(X_full)[:, 1]
 
# ROC curve
fpr_full, tpr_full, _ = roc_curve(y, pred_probs_full)
roc_auc_full = roc_auc_score(y, pred_probs_full)
 
# Plot and save
plt.figure()
plt.plot(fpr_full, tpr_full, label='Logistic Regression (area = %0.2f)' % roc_auc_full)
plt.plot([0, 1], [0, 1],'r--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Full Model')
plt.legend(loc="lower right")
plt.savefig('Logit_ROC_full.png')
plt.close()
 
# -----------------------------
# Decision-Use Model
# -----------------------------
 
# Drop variables not observable to lenders
decision_vars = credit.drop(columns=['default', 'bmaxrate', 'amount'])
X_decision = decision_vars
 
# Fit with statsmodels
X_decision_sm = sm.add_constant(X_decision)
logit_decision_model = sm.Logit(y, X_decision_sm).fit()
 
# Print summary results for README
print("\n--- DECISION MODEL SUMMARY ---\n")
print(logit_decision_model.summary())
 
# Fit using sklearn for ROC
logit_sk_decision = LogisticRegression(max_iter=1000)
logit_sk_decision.fit(X_decision, y)
pred_probs_decision = logit_sk_decision.predict_proba(X_decision)[:, 1]
 
# ROC curve
fpr_decision, tpr_decision, _ = roc_curve(y, pred_probs_decision)
roc_auc_decision = roc_auc_score(y, pred_probs_decision)
 
# Plot and save
plt.figure()
plt.plot(fpr_decision, tpr_decision, label='Logistic Regression (area = %0.2f)' % roc_auc_decision)
plt.plot([0, 1], [0, 1],'r--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Decision-Use Model')
plt.legend(loc="lower right")
plt.savefig('Logit_ROC_decision.png')
plt.close()
 
# -----------------------------
# End of File
# -----------------------------

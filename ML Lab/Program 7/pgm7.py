# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:26:49 2021

@author: Harsh
"""

import numpy as np
import csv
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('Pgm 7 heart.csv')

del heartDisease['oldpeak']
del heartDisease['slope']
del heartDisease['ca']
del heartDisease['thal']

heartDisease = heartDisease.replace('?',np.nan)

print(heartDisease.head())
model = BayesianModel([('age', 'heartdisease'), ('gender', 'heartdisease'), 
                       ('exang', 'heartdisease'),('trestbps','heartdisease'),('fbs','heartdisease'),
                      ('heartdisease','restecg'),('heartdisease','thalach'),('heartdisease','chol')])

model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('gender', 'trestbps'), ('gender', 'fbs'), 
                       ('exang', 'trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),
                      ('heartdisease','restecg'),('heartdisease','thalach'),('heartdisease','chol')])


model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)


print("Inferencing with Bayesian Network")

HeartDisease_infer = VariableElimination(model)

# Computing the probability of bronc given smoke.
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 28})
print(q)

q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'chol': 100})
print(q)
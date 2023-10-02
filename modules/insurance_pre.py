import os

import pickle
import time

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

import warnings
class InsurancePre():
    def __init__(self):
        pass
    
    def colPreparation(self):
        labelEncoder = ['Gender','Driving_License','Previously_Insured','Vehicle_Damage']
        oneHotEncoder = ['Vehicle_Age','Region_Code','Policy_Sales_Channel']
        scallingStandar = ['Age','Annual_Premium','Vintage']
    
        return labelEncoder, oneHotEncoder, scallingStandar
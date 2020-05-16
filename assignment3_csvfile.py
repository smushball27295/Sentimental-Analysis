# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:55:16 2020

@author: ramesh
"""

import pandas as pd


def csv(file):
    data = pd.read_csv(file)
    senti_data = pd.read_csv("final_csv.csv")
    for i in range(len(data)):
        name = data.iloc[i,0]
        purpose = data.iloc[i,1]
        senti_data = senti_data.append({'Name' : name, 'Purpose' : purpose},ignore_index=True)
    
    senti_data.to_csv("final_csv.csv",index=False)
    
    
csv("companies.csv")    
csv("ListOfCompanies JVansant.csv")





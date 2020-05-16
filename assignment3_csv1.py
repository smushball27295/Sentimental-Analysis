# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:04:01 2020

@author: ramesh
"""

#This file is used for csv that has extra column

import pandas as pd

file_5 = pd.read_csv("napu.csv")

df = file_5.drop(file_5.columns[[0]], axis=1)   

def csv1():
    data = df
    sent_data = pd.read_csv("final_csv.csv")
    for i in range(len(data)):
        name = data.iloc[i,0]
        purpose = data.iloc[i,1]
        sent_data = sent_data.append({'Name' : name, 'Purpose' : purpose},ignore_index=True)
    
    sent_data.to_csv("final_csv.csv",index=False)
    

if __name__ == "__main__":
    csv1()

    




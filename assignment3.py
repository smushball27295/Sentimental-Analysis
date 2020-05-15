# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:45:17 2020

@author: ramesh
"""

#This file is used to convert text files to csv
import re
import pandas as pd


def text(File_Name):
    file1 = open(File_Name,
             "r")
    data = file1.read()
    rx_name = re.compile(r'Name: (?P<name>.*)\n')
    rx_purpose = re.compile(r'Purpose: (?P<purpose>.*)')
    names = rx_name.findall(data)
    purposes = rx_purpose.findall(data)

    senti_data = pd.read_csv("final_csv.csv")
    for i in range(len(purposes)):
        senti_data = senti_data.append({'Name' : names[i], 'Purpose' : purposes[i]},ignore_index=True)

    senti_data.to_csv("final_csv.csv",index=False)


if __name__ == "__main__":
    text("595_HW2.txt")
    text("result.txt")
    text("Company_Details.txt")
    text("foryou4.txt")
    text("name_purpose.txt")
    text("output_Webscrap_HW2.txt")


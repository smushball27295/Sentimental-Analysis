# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 23:06:14 2020

@author: ramesh
"""

#file 1
errors = []                       # The list where we will store results.
linenum = 0
substr = "Name"         # Substring to search for.
with open ('webscrape_1.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.find(substr) != -1:    # if case-insensitive match,
            errors.append(line.rstrip('\n'))
for err in errors:
    print(err) 
    
linenum = 0
substr = "Purpose"         # Substring to search for.
with open ('webscrape_1.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.find(substr) != -1:    # if case-insensitive match,
            errors.append(line.rstrip('\n'))
for err in errors:
    print(err)  

#file4
linenum = 0
substr = "Purpose"         # Substring to search for.
with open ('webscrape_4.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.find(substr) != -1:    # if case-insensitive match,
            errors.append(line.rstrip('\n'))
for err in errors:
    print(err)   

                      # The list where we will store results.
linenum = 0
substr = "Name"         # Substring to search for.
with open ('webscrape_4.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.find(substr) != -1:    # if case-insensitive match,
            errors.append(line.rstrip('\n'))
for err in errors:
    print(err)       
    
    
#file8
linenum = 0
substr = "Purpose"         # Substring to search for.
with open ('webscrape_8.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.find(substr) != -1:    # if case-insensitive match,
            errors.append(line.rstrip('\n'))
for err in errors:
    print(err)       


errors = []                       # The list where we will store results.
linenum = 0
substr = "Name"         # Substring to search for.
with open ('webscrape_1.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.find(substr) != -1:    # if case-insensitive match,
            errors.append(line.rstrip('\n'))
for err in errors:
    print(err)   



x=[]
for i in h:
    blob = TextBlob(str(i))
    x.append(blob.sentiment)

i = 0
while i<len(errors):
    if errors[i][1]=='N' or errors[i][0]=='N':
        errors.remove(errors[i])
    i+=1

while i<len(errors):
    if errors[i][1]=='N':
        errors.remove(errors[i])
    i+=1
    
    
for i in range(len(x)):
    c.append(float(x[i].polarity))

len(c)


def Convert(lst): 
    res_dct = {lst[i]: i for i in range(0, len(lst))} 
    return res_dct    

s = Convert(errors) 
u = Convert(c)
for i in u.keys():
    r.append(i)
    
    
r.sort()
len(r)
for i in r:
    print(u[i])    
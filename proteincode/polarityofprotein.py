# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 01:38:20 2017

@author: Shivam
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:27:11 2017

@author: Shivam
"""
'''using an excel file i created a dictionary to count the type of
amino acids present in FASTA files'''
from collections import Counter
import xlrd
d={}
wb=xlrd.open_workbook('word.xlsx.')
sh=wb.sheet_by_index(0)
for i in range(sh.nrows):
    cell_value_class = sh.cell(i,1).value
    cell_value_id = sh.cell(i,0).value
    d[cell_value_class] = cell_value_id
'''This sets up the dictionary via the excel file'''

'''this prompts the user to input the protein file they wish to 
examine'''
file=input("what is the protein sequence file?")
protein= open(file,'r')
protein.readline() #skips the fasta header#
for new in protein:
    line = str.strip(new)
    print(line)
    n=[]
    for i in line:
        n.append(d[i])#uses dictionary value for keys#
    print(Counter(n))#counts occurence of values#
    

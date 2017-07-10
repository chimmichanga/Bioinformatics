# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:55:13 2017

@author: Shivam
"""

d={}
seq=''
with open('codon.txt','r') as dictionary:
    for line in dictionary:
        first=str.strip(line)
        (one,two) = first.split()
        d[one]=two
        d[two]=two   
    DNA =input('Your sequence filename is: ')
    fh = open(DNA, 'r')
    
    fh.readline()
    for line in fh:
        line = str.strip(line)
        seq = seq + line
    length = len(seq)
    countA = seq.count('A')
    countT = seq.count('T')
    countC = seq.count('C')
    countG = seq.count('G')
    print (seq)
    print ('The length of your sequence is' ,length, 'bases')
    for i in range(length-3):
        data=seq[i]+seq[i+1]+seq[i+2]
        print ('The' ,i+1, '3mer is' ,data,)

flag = 3
count = 0
protein = ''
while flag:
    if count >= len(seq):
        flag = 0 
    now = seq[count:count + 3]
       	 
    if now=="TGA":
        break
    if now =="TAA":
        break
    if now=="TAG":
        break
    if now in d:
        if now == "ATG":
            protein = protein + d[now]
        protein = protein + d[now]      
    count += 3

found = protein.find("M");
if found == -1:
    print("NOT FOUND")
else:
    protein = protein[found:]
    print("The protein sequence is: " + protein[1:])
    print("The length of the protein is: " + str(len(protein)) + " amino acids")

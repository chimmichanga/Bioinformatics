# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 00:55:50 2017

@author: Shivam
"""

dna=input('what is your filename?')
s= open (dna,'r')
seq=s.read()
'''this opens the file in a read only format based on the user
inputting the file name'''
print('The DNA sequence is:'+seq)

'''this loop allows the strand to get its complement based on looping
through the file character by character and appending complementary
bases in list'''
complement=[]
for base in seq:
    if base=='A':
        complement.append('T')
    elif base == "T":
        complement.append("A")
    elif base == "C":
        complement.append("G")
    elif base == "G":
       complement.append("C")
comp=''.join(complement)


'''similar process in this as the designing of the complementary strand'''
rna=[]
for nucleotide in seq:
    if nucleotide=='T':
        rna.append('U')
    elif nucleotide == "A":
        rna.append("A")
    elif nucleotide == "G":
        rna.append("G")
    elif nucleotide == "C":
       rna.append("C")
rna=''.join(rna)

print('The complementary strand is:'+ comp)
print('The RNA strand for this DNA sequence is:'+rna)



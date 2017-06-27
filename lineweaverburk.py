# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:23:12 2017

@author: Shivam
"""

'''this is a program that seeks to produce a lineweaver-burk plot
that will visualize the data in a plot and show the Km value and the Vmax for
the enzyme based on scientists' data and inputs'''

import matplotlib.pyplot as plt
import numpy as np

experiments=int(input("how many trials did you run"))
#as the scientist for number of trials#

enzyme= []
speed=[]
#generates a list to hold values for x and y axis#
for i in range(experiments):#initiates the loop#

    data=(1/int(input("What is substrate concentration")))
    enzyme.append(data)
    velocity=(1/int(input("What is the velocity")))
    speed.append(velocity)
#using the for loop the lists are filled with values for x and y#


slope,intercept=np.polyfit(enzyme,speed,1)
print("The Km/Vmax is:",slope)
print('The Vmax is:',1/intercept)
print('The Km is:',slope/intercept)
#Prints out the values for Km, Vmax, and the slope#

abline_values=[slope*i +intercept for i in enzyme]

plt.plot(enzyme,abline_values,'b')
plt.title('Lineweaver Burk Plot',fontsize=30)
plt.xlabel('1/concentration',fontsize=20)
plt.ylabel('1/Velocity',fontsize=20)
plt.plot(enzyme,speed,'ro')
plt.show()

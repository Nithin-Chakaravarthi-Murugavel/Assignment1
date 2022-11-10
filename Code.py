# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 22:28:25 2022

@author: nithi
"""
# To plot the graph
import matplotlib.pyplot as plt
# Used to read the csv file
import pandas as pd
# Creating a varaiable and stores the csv file data in it.
read_data = pd.read_csv(r'D:\Applied Data Science 1\Assignment_1\All Countries.csv')
print(read_data)
# .loc is used to access a sepcific country from the column
selectedCountry=read_data.loc[read_data['Location'] == 'South Africa']
selectedCountry2=read_data.loc[read_data['Location'] == 'Congo']
selectedCountry3=read_data.loc[read_data['Location'] == 'Egypt']
selectedCountry4=read_data.loc[read_data['Location'] == 'Indonesia']
# Creating Varaible x,y,w,u to store the selected country's year and its value
x = selectedCountry['Period']
y = selectedCountry['Value']
w = selectedCountry2['Period']
u = selectedCountry2['Value']
plt.figure()
# Line Plot the x and y function. Label are used to produce legend
plt.plot(x,y,label='South Africa')
plt.plot(w,u,label='Congo')
# Used to label the x-axis and y-axis
plt.xlabel('Year')
plt.ylabel('Percentage (%)') 
#To Name the title for the graph 
plt.title('TB Patients with HIV')
# Add the legend and loc is used to produce the legend in specific side of the graph
plt.legend(loc='lower right')
# To Remove the whitespace from x-axis
plt.margins(x=0)
# To show the graph
plt.show()
plt.figure()
# Pie plotting the specific countries year
# autopct is used to specify the percentage for each silce of pie
# explode is used to seprate the slice from the pie
plt.pie(selectedCountry3['Value'],labels=selectedCountry3['Period'],
        autopct= '%1.2f%%',explode=(0.2,0,0,0.2,0,0,0))
plt.title("Egypt TB Patients with HIV")
plt.show()
plt.figure()
# Bar plotting the counties percentage in y-axis and years in x-axis
plt.bar(selectedCountry4['Period'],selectedCountry4['Value'],label='Indonesia')
plt.xlabel('Year')
plt.ylabel('Percentage (%)') 
plt.title('TB Patients with HIV')
plt.legend()
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:50:45 2023

@author: Harikrishnan Marimuthu
"""

# Importing the packages:
import pandas as pd
import matplotlib.pyplot as plt


# Define a function to produce a line plot:
def line_plot(fsa_data):
    """
    Plot a line graph showing the number of cases commenced and the number of successful cases by area.

    Parameters:
    - fsa_data (DataFrame): DataFrame containing relevant data.

    Returns:
    - None
    """
    grouped1 = fsa_data.groupby('Area')['Number_Of_Cases_Commenced'].sum().reset_index()
    grouped2 = fsa_data.groupby('Area')['Number_Of_Successful_Cases'].sum().reset_index()
   
    plt.figure(figsize=(12, 6))
    plt.plot(grouped1['Area'], grouped1['Number_Of_Cases_Commenced'])
    plt.plot(grouped2['Area'], grouped2['Number_Of_Successful_Cases'])
    plt.xlabel('Area')
    plt.ylabel('Number of Cases')
    plt.title('Number of Prosecution Cases by Area')
    plt.grid(True)
    plt.legend(['Number of Cases Commenced', 'Number of Successful Cases'])
    plt.show()

# Define a function to produce a bar plot:
def bar_plot(fsa_data):
    """
    Plot a bar graph showing the total fines by area.

    Parameters:
    - fsa_data (DataFrame): DataFrame containing relevant data.

    Returns:
    - None
    """
    grouped3 = fsa_data.groupby('Area')['Total_Fines'].sum().reset_index()
   
    plt.figure(figsize=(12, 6))
    plt.xlabel('Area')
    plt.ylabel('Total Fines')
    plt.title('Total Fines by Area')
    plt.bar(grouped3['Area'], grouped3['Total_Fines'], color='skyblue', width=0.4)
    plt.legend(['Total Number Of Fines'])
    plt.show()

# Define a function to produce a scatter plot:
def scatter_plot(fsa_data):
    """
    Plot a scatter graph showing the relationship between total costs and total fines.

    Parameters:
    - fsa_data (DataFrame): DataFrame containing relevant data.

    Returns:
    - None
    """
    plt.figure(figsize=(12, 6))
    costs_color = 'red'
    fines_color = 'blue'
    plt.scatter(fsa_data['Total_Costs'], fsa_data['Total_Fines'], c=costs_color)
    plt.scatter(fsa_data['Total_Fines'], fsa_data['Total_Costs'], c=fines_color)
    plt.title('Total Costs vs Total Fines')
    plt.xlabel('Total Costs')
    plt.ylabel('Total Fines')
    plt.legend(['Total Costs', 'Total Fines'])
    plt.show()

# Reading data from the respective path and cleaning the data:
file_path = pd.read_csv("./datas.csv")
fsa_data = pd.DataFrame({'Period_Start': file_path.PeriodStart, 'Period_End': file_path.PeriodEnd, 'Area': file_path.Area, 'Number_Of_Cases_Commenced': file_path.NumberOfCasesCommenced, 'Number_Of_Successful_Cases': file_path.NumberOfSuccessfulCases, 'Companies_Or_Individuals_Successfully_Prosecuted': file_path.CompaniesOrIndividualsSuccessfullyProsecuted, 'Inf_Files_CoveredBy_Successful_Cases': file_path.InfFilesCoveredBySuccessfulCases, 'Total_Fines': file_path.TotalFines, 'Total_Costs': file_path.TotalCosts})
fsa_data.dropna(subset=['Period_Start', 'Period_End', 'Area', 'Number_Of_Cases_Commenced', 'Number_Of_Successful_Cases', 'Companies_Or_Individuals_Successfully_Prosecuted', 'Inf_Files_CoveredBy_Successful_Cases', 'Total_Fines', 'Total_Costs'], inplace=True)

# Function call (line,bar,scatter):
line_plot(fsa_data)
bar_plot(fsa_data)
scatter_plot(fsa_data)
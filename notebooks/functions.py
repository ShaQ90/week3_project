# Our functions go here
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import random

#Functions to make a plot from pivot_tabel with index and values

def takes_x_values (df):
    x_values = []
    for item in df.index:
        x_values.append(item)
    return x_values

def takes_y_values (df, column_name):
    y_values = []
    for item in df[column_name]:
        y_values.append(item)
    return y_values

def number_positions(number):
    positions = []
    for x in range(1,number+1):
        positions.append(x)
    return positions

#fuction to add label to income
def income_label (value):
    #values from research
    
    if value < 28000 :
        return "lower"
    elif value < 90000:
        return "middle"
    else:
        return "higher"

#fucntion to draw plot graph for DF with index and value
    
def plot_drawing_single(df, agg_opt,):

    tick_label = takes_x_values(df)
    # plotting a bar chart
    plt.bar(number_positions(len(df)),
             takes_y_values(df,df.columns[0]),
             tick_label = tick_label,
             width = 0.8,
             color = ['red', 'green'])
    
    # naming the x-axis
    plt.xlabel(df.index.name)
    # naming the y-axis
    plt.ylabel(df.columns[0])
    # plot title
    plt.title(df.columns[0]+" per "+df.index.name +" ("+ agg_opt+")")
    #save plot
    plt.draw()
    filename= df.columns[0]+"x"+df.index.name +"("+ agg_opt+")"
    plt.savefig("../figures/"+filename.replace(' ','_')+".png")
    #display plot
    plt.show()

def plot_drawing_pie_count(df):
    # Creating labels
    label_names = takes_x_values(df)
    total_values = 0
    label_values = []
    for x in range(len(df)):
        total_values += int(df.values[x])
        label_values.append(int(df.values[x]))

    for x in range(len(label_values)):
        precentage = int((label_values[x])*100)/ int(total_values)
        label_names[x] += "\n"+str(round(precentage,2))+" %"

    
    #Creating plot
    #fig = plt.figure(figsize=(10, 7))
    plt.pie(label_values, labels=label_names)

    # plot title
    plt.title(df.index.name+" Percentages")
    #save plot
    plt.draw()
    filename= df.columns[0]+"x"+df.index.name 
    plt.savefig("../figures/"+filename.replace(' ','_')+".png")
    #display plot
    plt.show()


def get_col_names(df):
    col_names = []
    for x in df.columns:
        col_names.append(x)

    return col_names


#fucntion to draw stacked graph for DF with multiple functions

def plot_drawing_sg(df, agg_opt, value_name):
    
    num_rows = df.shape[0]
    col_names = get_col_names(df)
#starts the list for the sum of values adn rows names
    totals = []
    rows_names=[]
    for x in range(len(col_names)):
        totals.append(0)

#get all values to a list 
    for x in range(num_rows):
        value = []
        for y in col_names:
            value.append(float(df[y].iloc[x]))
    
#First row doesnt need a bottoms parameter
        if x == 0:
            plt.bar(col_names, np.asarray(value), color =(round(random.random(),2),round(random.random(),2),round(random.random(),2)))
        else:
            plt.bar(col_names, np.asarray(value), bottom = np.asarray(totals), color=(round(random.random(),2),round(random.random(),2),round(random.random(),2)))
            
        for y in range(len(col_names)):
            totals[y] += value[y]
            
#Get tthe names of the rows    
        rows_names.append(df.index[x])
    

    plt.xlabel(df.columns.name)
    plt.ylabel(value_name)
    plt.legend(rows_names)
    plt.title(df.index.name+" vs "+df.columns.name+" ("+agg_opt+")")
    filename= df.columns[0]+"x"+df.index.name +"("+ agg_opt+")"
    plt.savefig("../figures/"+filename.replace(' ','_')+".png")
    plt.show()       
    
    

#fuction to make age groups
def age_group (age):
    if age > 90 :
        return 90
    elif age > 80:
        return 80
    elif age > 70:
        return 70
    elif age > 60:
        return 60
    elif age > 50:
        return 50
    elif age > 40:
        return 40
    elif age > 30:
        return 30
    elif age > 20:
        return 20
    elif age > 10:
        return 10
    else:
        return 0

def creat_df_count (df, col):

    df = pd.DataFrame(df[col].value_counts())
    df.index.name = col
    df.columns = ['count']
    return df


# Our functions go here
import pandas as pd
import os
import matplotlib.pyplot as plt
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


#fucntion to draw plot graph for single DF
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


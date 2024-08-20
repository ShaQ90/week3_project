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

def plot_drawing(df, agg_opt):
    
    tick_label = takes_x_values(df)
    # plotting a bar chart
    plt.bar(number_positions(len(df)),
             takes_y_values(df,df.columns[0]),
             tick_label = tick_label,
             width = 0.8,
             color = ['red', 'green'])
    
    print(len(df) , takes_y_values(df,df.columns[0]),takes_x_values(df) )
    # naming the x-axis
    plt.xlabel(df.index.name)
    # naming the y-axis
    plt.ylabel(df.columns[0])
    # plot title
    plt.title(df.columns[0]+" per "+df.index.name +" ("+ agg_opt+")")
    plt.show()
    return 1
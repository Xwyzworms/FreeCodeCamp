import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    y2 = []
    y3= []
    # Create scatter plot
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    years1 = list(range(1880,2050))
    years2 = list(range(2000,2050))
    for year in years1:
      y2.append(intercept + slope * year)
    
    x = df[df["Year"] >= 2000]
    y = x["CSIRO Adjusted Sea Level"]
    x = x['Year']
   
    slope, intercept, r_value, p_value, std_err = linregress(x,y)    
    for year in years2:
      y3.append(intercept + slope * year)

    plt.plot(years1,y2,'r', label = 'Bests Fit Line 1')
  
    # Create second line of best fit
    plt.plot(years2,y3,label = 'Bests Fit Line 2')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
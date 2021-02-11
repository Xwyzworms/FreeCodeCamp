import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def getOverweight(weight,height):
    BMI = weight / (height / 100)**2
    if BMI > 25 :
        return 1
    else:
        return 0
# Use this if you want to do many condition for each data ..
def CleanIt(ap_lo,ap_hi,height,weight,df):
    heightLowPercentile = np.quantile(df["height"],0.025,axis=0)
    heightHighPercentile = np.quantile(df["height"],0.975,axis=0)
    WeightLowPercentile = np.quantile(df["weight"],0.025,axis=0)
    WeightHighPercentile = np.quantile(df["weight"],0.975,axis=0)
    
    diastolic_press = ap_lo <= ap_hi
    isCorrectHeight = (height > heightLowPercentile) and (height < heightHighPercentile)
    isCorrectWeight = (weight > WeightLowPercentile) and (weight < WeightHighPercentile)
    return diastolic_press and isCorrectHeight and isCorrectWeight


# Import data
df = pd.read_csv("medical_examination.csv")
print("SnowUp")
# Add 'overweight' column
df['overweight'] = df.apply(lambda x :getOverweight(x["weight"],x["height"]),axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = df["cholesterol"].apply(lambda x : 1 if x > 1 else 0 )
df["gluc"] = df["gluc"].apply(lambda x: 1 if x > 1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    melted = pd.melt(df,id_vars=["cardio"],value_vars=["active","alco","cholesterol","gluc","overweight","smoke"])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    melted["total"] = 1
    df_cat_splitted = melted.groupby(["cardio","variable","value"],as_index=False).count()
    # Draw the catplot with 'sns.catplot()'

    fig=sns.catplot(data = df_cat_splitted,x="variable",y="total",kind="bar",col="cardio",ci=None,hue="value")  


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig.fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= (df['height'].quantile(0.025))) &
    (df['height'] <= (df['height'].quantile(0.975))) &
    (df['weight'] >= (df['weight'].quantile(0.025))) &
    (df['weight'] <= (df['weight'].quantile(0.975)))
    ]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax =  plt.subplots(1,1,figsize=(10,10))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr,mask=mask,linewidths=1,annot=True,vmax=.30,center=0.08,square=True,cbar_kws = {'orientation' : 'vertical'},fmt=".1f")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

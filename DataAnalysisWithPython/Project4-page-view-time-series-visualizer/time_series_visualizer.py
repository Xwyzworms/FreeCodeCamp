import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates = ['date'], index_col ='date')
# Clean data
df = df[(df["value"] >=df["value"].quantile(0.025)) &
          (df["value"] <=df["value"].quantile(0.975))]
months = ['January', 'February', 'March', 'April' , 'May' , 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(1,1,figsize=(14,6))
    ax.plot(df.index,df["value"],color="r")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    dfcopy = df.copy()
    dfcopy["month"] = dfcopy.index.month_name()
    dfcopy["year"] = dfcopy.index.year
   
    dfcopy["month"] = pd.Categorical(dfcopy['month'], categories=months, ordered=True)    
    ans = dfcopy.groupby(["year","month"])["value"].mean().unstack()
    ansFig = ans.plot(kind="bar",figsize=(14,8)).figure
    plt.ylabel("Average Page Views")
    plt.xlabel("Years")
    plt.legend(labels=months,title="Months")

    # Save image and return fig (don't change this part)
    ansFig.savefig('bar_plot.png')
    return ansFig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months, ordered=True)

    # Draw box plots (using Seaborn)
    fig,ax = plt.subplots(1,2,figsize=(20,5))
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
  
    sns.boxplot(x = df_box["year"],y = df_box.value,ax=ax[0])
    sns.boxplot(x = df_box["month"],y = df_box.value,ax=ax[1])
    ax[0].set_xlabel("Year")
    ax[1].set_xlabel("Month")
    ax[0].set_ylabel("Page Views")
    ax[1].set_ylabel("Page Views")





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

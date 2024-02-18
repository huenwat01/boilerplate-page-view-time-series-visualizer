import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date')

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(35,10))
    ax.plot(df.index,df['value'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    month = {"01":"January",
             "02":"February",
             "03":"March",
             "04":"April",
             "05":"May",
             "06":"June",
             "07":"July",
             "08":"August",
             "09":"September",
             "10":"October",
             "11":"November",
             "12":"December"
            }
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    df_bar['year'] = [d[0:4] for d in df_bar['date']]
    df_bar['month'] = [month[str(d[5:7])] for d in df_bar['date']]
    temp = pd.DataFrame(df_bar.groupby(['year','month'])['value'].mean())
    temp.reset_index(inplace=True)
    temp['month'] = pd.Categorical(temp['month'], categories=months)
    print(temp.dtypes)
    #df_bar['avg'] = df_bar.groupby(['year','month'])['value'].mean()
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10,10))
    ax = sns.barplot(temp, x="year", y="value", hue="month")
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    month = {"01":"Jan",
             "02":"Feb",
             "03":"Mar",
             "04":"Apr",
             "05":"May",
             "06":"Jun",
             "07":"Jul",
             "08":"Aug",
             "09":"Sep",
             "10":"Oct",
             "11":"Nov",
             "12":"Dec"
            }
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['year'] = [d[0:4] for d in df_box['date']]
    df_box['month'] = [month[str(d[5:7])] for d in df_box['date']]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months)
    # Draw box plots (using Seaborn)    
    fig, ax = plt.subplots(1,2,figsize=(18,6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df_box['year'], y=df_box['value']).get_figure()
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df_box['month'], y=df_box['value']).get_figure()
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

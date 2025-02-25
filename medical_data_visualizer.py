import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# useful to know the column header names
print(df.keys())

# 2
'''
First calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
'''
# Weight already in kg, height in cm
BMI = df['weight']/(df['height'] /100)**2

#print('BMI', BMI)


df['overweight'] = (BMI > 25).astype(int) # True = 1, False = 0
#print(df['overweight'])

# 3
'''
Normalize data by making 0 always good and 1 always bad. 
If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
'''
# print(df['gluc'].value_counts()) # Can be 1, 2 or 3
# print(df['cholesterol'].value_counts()) # Can be 1, 2 or 3

df[['gluc', 'cholesterol']] = df[['gluc', 'cholesterol']].replace([1, 2, 3], [0, 1, 1])
# print(df[['gluc', 'cholesterol']])
# print(df['gluc'].value_counts())

# 4
def draw_cat_plot():
    # 5
    '''
    Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    '''
    df_cat = pd.melt(df, id_vars=['id', 'cardio'], 
    value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='Condition', value_name='Health score')
    print(df_cat)


    # 6
    '''
    Group and reformat the data in df_cat to split it by cardio. 
    Show the counts of each feature. 
    You will have to rename one of the columns for the catplot to work correctly.
    '''

    df_cat = pd.melt(df, id_vars=['id', 'cardio'], 
    value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='Condition', value_name='Health score')
    print(df_cat)
    

    # 7
    '''
    Convert the data into long format and 
    create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: sns.catplot().
    '''



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig
draw_cat_plot()

# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig

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
- First calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
    If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
'''
# Weight already in kg, height in cm
BMI = df['weight']/(df['height'] /100)**2

#print('BMI', BMI)


df['overweight'] = (BMI > 25).astype(int) # True = 1, False = 0
#print(df['overweight'])

# 3
'''
- Normalize data by making 0 always good and 1 always bad. 
- If the value of cholesterol or gluc is 1, set the value to 0. 
    If the value is more than 1, set the value to 1.
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
    - Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    '''

    df_cat = pd.melt(df, id_vars=['cardio'], 
    value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='variable', value_name='variable score')
    print(df_cat)
    print(df_cat.shape)
    # Melts wide data to creates a long table with four columns
    # ID/ cardio score/ condition name / associated 0-1 point of condition score


    # 6
    '''
    - Group and reformat the data in df_cat to split it by cardio. 
    - Show the counts of each feature. 
    - You will have to rename one of the columns for the catplot to work correctly.
    '''
    df_cat = df_cat.groupby(['cardio']).value_counts().reset_index(name='total')

    

    # 7
    '''
    - Convert the data into long format and 
        create a chart that shows the value counts of the categorical features 
        using the following method provided by the seaborn library import: sns.catplot().
    '''

    # Test code specifies that x labels should be in alphabetical order, I can use sort_values() for this.
    df_cat = df_cat.sort_values(by='variable', ascending = True)
    cat_plot = sns.catplot(data = df_cat, kind="bar", x = "variable", y = "total", hue = "variable score", col = "cardio")


    # 8
    fig = cat_plot.fig


    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    '''
    - Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
        diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    - height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    - height is more than the 97.5th percentile
    - weight is less than the 2.5th percentile
    - weight is more than the 97.5th percentile

    Systolic blood pressure df['ap_hi']
    Diastolic blood pressure df['ap_lo']
    '''

    df_heat =df[(df['ap_lo'] <= df['ap_hi']) 
                & (df['height'] >= df['height'].quantile(0.025))
                & (df['height'] <= df['height'].quantile(0.975)) 
                & (df['weight'] >= df['weight'].quantile(0.025))
                & (df['weight'] <= df['weight'].quantile(0.975)) ]

    # 12
    '''
    - Calculate the correlation matrix and store it in the corr variable.
    '''
    corr = df_heat.corr()


    # 13
    '''
    - Generate a mask for the upper triangle and store it in the mask variable.
    '''
    # Initialise shape of mask to be identical to shape of corr
    mask = np.triu(np.ones(corr.shape), k=0)
    # Setting k = 0 makes explicit that the diagonal is included in the upper triangle mask
    # As seen in Figure_2.png, want the diagonal to be masked along with the upper tri.
   
    #print(mask) # Checking mask is as expected



    # 14
    '''
    - Set up the matplotlib figure.
    '''
    fig, ax = plt.subplots(figsize = (12, 10))

    # 15
    '''
    - Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
    '''
    # Test code calls for 1 decimal place like in fig 1, use fmt parameter
    ax = sns.heatmap(data = corr, mask = mask, annot = True, fmt = ".1f", cmap = "magma")


    # 16
    fig.savefig('heatmap.png')
    return fig

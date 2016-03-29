#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import pandas as pd
import math

#getting the file from github into a table
url = 'https://raw.githubusercontent.com/andysevas/dsp/master/python/football.csv'
df = pd.read_csv(url)

#creating a new column for Goal Differential
df['Goal Diff'] = (df['Goals']-df['Goals Allowed'])

#Taking the absolute value of that column, so I can find the smallest differential in magnitude
df['Abs Goal Diff'] = abs(df['Goal Diff'])

#locating the minimum
smallest_goal_diff = df.loc[df['Abs Goal Diff'] == (df['Abs Goal Diff']).min()]

#Explicitly calling out the team.  
smallest_goal_diff['Team']

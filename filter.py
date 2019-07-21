import pandas as pd
import numpy as np



df = pd.read_csv('Canadian_Creditcard_Bin.csv', encoding = "ISO-8859-1")


# first input from user
# input string is 'input_string'

input_rewards = input('Which Reward Program appeals to you more?\n 1: Flexible Rewards \n 2: Travel Rewards \n 3: Cashback \n' )



if(input_rewards == '1'):
	df_rewards = df.loc[df['Reward Program'].isin(['Membership Rewards Select', 'Membership Rewards', 'BMO Rewards', 'WestJet Dollars', 'RBC Rewards', 'Scotia Rewards', 'More Rewards', 'Aspire', 'American Express Invites'])]

elif(input_rewards == '2'):
	df_rewards = df.loc[df['Reward Program'].isin(['Sky', 'Air Miles', 'Aeroplan', 'Aventura', 'Alaska Miles', 'Best Western', 'Avion', 'Asia Miles', 'Scene Points', 'TD Travel Rewards'])]

else:
	df_rewards = df.loc[df['Reward Program'].isin(['Cashback'])]




print(df_rewards)

#df['Sign-Up Bonus'] = df['Sign-Up Bonus'].str.replace(',', '')
#df['Sign-Up Bonus'] = pd.to_numeric(df['Sign-Up Bonus'], errors='coerce')
#df.loc[df['Sign-Up Bonus'] > 0, 'Sign-Up Bonus Bin'] = 1
#df.loc[df['Sign-Up Bonus'] <= 0, 'Sign-Up Bonus Bin'] = 0
#df['Sign-Up Bonus'].apply(str)
#df = df.drop(['Sign-Up Bonus'], axis=1)
#df['Sign-Up Bonus Bin'].apply(str)

# df_merged = pd.merge(df, binFile)
# print(df_merged)
# df_merged.to_csv('Canadian_Creditcard_Bin.csv')


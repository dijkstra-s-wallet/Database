import pandas as pd
import numpy as np



df = pd.read_csv('confirm_database.csv', encoding = "ISO-8859-1")
binFile = pd.get_dummies(df, columns = ['Reward Program', 'Charge or Credit Card?'])
#df = df.drop(['Reward Program', 'Charge or Credit Card?'], axis=1)
#df['Sign-Up Bonus'] = df['Sign-Up Bonus'].str.replace(',', '')
#df['Sign-Up Bonus'] = pd.to_numeric(df['Sign-Up Bonus'], errors='coerce')
#df.loc[df['Sign-Up Bonus'] > 0, 'Sign-Up Bonus Bin'] = 1
#df.loc[df['Sign-Up Bonus'] <= 0, 'Sign-Up Bonus Bin'] = 0
#df['Sign-Up Bonus'].apply(str)
#df = df.drop(['Sign-Up Bonus'], axis=1)
#df['Sign-Up Bonus Bin'].apply(str)

df_merged = pd.merge(df, binFile)
print(df_merged)
df_merged.to_csv('Canadian_Creditcard_Bin.csv')

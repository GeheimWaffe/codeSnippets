import pandas as pd

from dataframegenerator import generate_dataframe_1

def print_text(value: str):
    print('*** ' + value)

df = generate_dataframe_1()
gd = df.groupby('Lieu', as_index=True).mean()

print_text('this is the whole dataframe')
print(gd)
print_text('selecting a column')
print(gd['Temperature'])
print_text('*** retry : grouping on a specific columns')
gd = df[['Lieu', 'Pressure']].groupby('Lieu', as_index=True).sum()
print(gd)
print_text('try accessing the index directly')
print(gd.loc['Campagne']) # important conclusion : you have to use loc with []




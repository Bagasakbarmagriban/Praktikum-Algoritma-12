# -*- coding: utf-8 -*-
"""Latihan 1ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_s0BzUD-mN-ARlmh9osS5JwZYI1LQYk9
"""

import pandas as pd

df = pd.read_csv(r'/content/Negara.csv')
numeric_columns = df.select_dtypes(include=['number']).columns
rata = df.groupby(['Benua'])[numeric_columns].mean()
std = df.groupby(['Benua'])[numeric_columns].std()

print('DATA FRAME')
print(df)
print('=========================================================')
print('DATA MEAN')
print(rata)
print('=========================================================')
print('DATA DEVIATION')
print(std)
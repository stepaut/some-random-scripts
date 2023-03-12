import numpy as np
import pandas as pd
from datetime import datetime

df = pd.read_csv('TimeStatistics\data.txt')
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(df.info())

activities = df.Activity.unique()

first_year = df.Start.min().year
last_year = df.End.max().year

for year in range(first_year, last_year + 1):
    dfy = pd.DataFrame(columns=np.hstack(['week', activities]))
    print(dfy)

    break
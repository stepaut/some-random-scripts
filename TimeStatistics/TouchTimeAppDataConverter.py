import numpy as np
import pandas as pd
from datetime import datetime

df = pd.read_csv('TimeStatistics\data.txt')
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(df.info())


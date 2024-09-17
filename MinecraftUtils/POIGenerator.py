import pandas as pd

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import openfilegui

file = openfilegui.gui_fname("").decode()
df = pd.read_csv(file, on_bad_lines="warn", sep=",")

res = "'manualpois':[\n"

len = len(df)

for index, row in df.iterrows():
    id = row['type']
    if row['ready'] == "yes":
        id += "Ready"

    res += "{"
    res += f"'id':'{id}',\n"
    res += f"'x':{row['x']},\n"
    res += "'y':64,\n"
    res += f"'z':{row['z']},\n"
    res += f"'name':\"{row['name']}\""
    if (index != len - 1):
        res += "},\n"
    else:
        res += "}],"

print(res)

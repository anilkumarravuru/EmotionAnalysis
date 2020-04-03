# Anil Kumar Ravuru

import pandas as pd

df = pd.read_json('../Project/fb_data.json')
print(df.columns)
useful_cols = ['fb_like', 'fb_angry', 'fb_thankful', 'fb_haha', 'description', 'fb_sad', 'message', 'fb_wow', 'fb_love']
xdf = df[useful_cols]
print(xdf['message'].count())
print(xdf.columns)
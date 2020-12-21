import os
import numpy as np
import pandas as pd

db = pd.DataFrame(columns=['pic', 'num', 'x','y','w','h'],index = range(0,303)) # 303 is the total number of images
entries = os.listdir('C:/Users/opera_user/PycharmProjects/FaceDet/test')
for j in range(0, 303):
    print(j)
    vid = int(entries[j].split('p')[0])
    frame = int(entries[j].split('p')[1].split('.')[0])
    df = pd.read_csv(f'C:/Users/opera_user/Documents/sfresh/{vid}.txt', header=None, delimiter = '\t')
    for i in range(0,len(df)):
        if df.values[i,0] == frame:
            db.loc[j,'pic'] = entries[j]
            db.loc[j,'num'] = df.values[i,1]
            db.loc[j, 'x'] = df.values[i,2]
            db.loc[j, 'y'] = df.values[i,3]
            db.loc[j, 'w'] = df.values[i,4]
            db.loc[j, 'h'] = df.values[i, 5]

np.savetxt(f'C:/Users/opera_user/Documents/important.txt', db.values, delimiter='\t',  fmt='%s')  # saving as .txt
#print('done')

import numpy as np
import pandas as pd

for i in range(0,315):
    annot = pd.read_csv(f'C:/Users/opera_user/Documents/folder/{i}.txt', delimiter=' ', header=None,error_bad_lines=False) # reading object annotation files given in VIRAT Dataset
    df = annot[annot[7] == 1] # filtering out annotations only for humans
    df = df.drop(columns = [0, 1, 7]) # Dropping unnecessary columns
    df = df.sort_values(by=2) # Sorting by frame no.
    df.insert(1, value=1, column='t') # insert number of objects to use it for opencv training
    np.savetxt(f'C:/Users/opera_user/Documents/sfresh/{i}.txt', df.values, fmt='%d', delimiter = '\t') # saving as .txt

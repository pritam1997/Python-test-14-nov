import pandas as pd
import os,glob
import math

path= '20191101/'
files = glob.glob(path+"*.csv")
filenames = os.listdir('20191101')



def file_to_df(files, filenames):

    base1 = os.path.splitext(filenames)

    b1 = base1[0].split(" ")
    symbol = b1[0]
    date = b1[1] + " " + b1[2] + " " + b1[3]
    option = b1[4]

    if(b1[5].find(".")):
        f = float(b1[5])
        strike = math.floor(f)
    else:
        strike= float(b1[5])
    # print(strike)

    df = pd.read_csv(files)
    c = 0
    for i in df.iterrows():
        c += 1
    # no of rows in file


    sym = []
    dt = []
    optiontype = []
    sp = []
    for i in range(c):
        sym.append(symbol)
        dt.append(date)
        optiontype.append(option)
        sp.append(strike)

    df.insert(0, 'Symbol', sym)
    df.insert(1, 'ExpiryDate', dt)
    df.insert(2, 'OptionType', optiontype)
    df.insert(3, 'StrikePrice', sp)
    return df



dtf=[]
for i in range(len(files)):
    dtf.append(file_to_df(files[i], filenames[i]))

f = pd.concat(dtf)

f.to_csv('20191101.csv')

print("merging done")


import pandas as pd
import os
import math
#
arr = os.listdir('C://Users//panka//Desktop//pritam//programs//20191101//')
# df2 = pd.read_csv('ABC 01 NOV 19 CALL 86.5.csv')
# print(df1)
# df3 = pd.concat([df1,df2])
# df3.to_csv('1.csv')
# df = pd.read_csv('1.csv')
print(arr)

def file_to_df(filenames):

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

    df = pd.read_csv(filenames)
    c = 0
    for i in df.iterrows():
        c += 1
    # no of rows in file

    df = pd.read_csv(filenames)

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


# df1 = file_to_df(file1)
# df2 = file_to_df(file2)
# print(df2)
#
# df3 = pd.concat([df1,df2])
# df3.to_csv('20191101.csv')

#
dtf=[]
for i in arr:
    file=i;
    dtf.append(file_to_df(file))

f = pd.concat(dtf)

# f.to_csv('1.csv')
# print(f)


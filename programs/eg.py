import multiprocessing as m
def some():
    print("function")

p = m.Process(target=some)
p.start()

# import pandas as pd
# import glob,os
#
# path= '20191101/'
#
# files=glob.glob(path+"*.csv")
#
# l = os.listdir(path)
#
# print(files)
#
# df = pd.read_csv(files[0])
# print(df)
#

# for f in l:
# 	ed = pd.read_csv(f)
# 	df.append(ed)
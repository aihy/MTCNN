from crop_face import cc
import os
import progressbar

num = 0
fp = open("all_list.txt","w")
for root,dirs,files in os.walk("/home/zihao_wang/data5/deception/deception_frame/"):
    for name in files:
        i=os.path.join(root,name)
        o=i.replace("deception_frame","deception_face")
        if "Deceptive" in o:
            print(o+" 0",file=fp)
        else:
            print(o+" 1",file=fp)


import pandas as pd

dfl=pd.read_csv("all_list.txt",delimiter=' ')
train_data=dfl.sample(frac=0.75,random_state=0,axis=0)
len(train_data)

val_data=dfl[~dfl.index.isin(train_data.index)]
len(val_data)

train_data.to_csv("train_data.csv",index=False)
val_data.to_csv("val_data.csv",index=False)

print(train_data.iloc[0])

sample_train_data=dfl.sample(n=200,random_state=1,axis=0)
temp=dfl[~dfl.index.isin(train_data.index)]
sample_val_data=temp.sample(n=100,random_state=1,axis=0)
len(sample_train_data)
len(sample_val_data)
sample_train_data.to_csv("sample_train_data.csv",index=False)
sample_val_data.to_csv("sample_val_data.csv",index=False)



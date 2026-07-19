#group  data by categoprical column
import pandas as pd

data ={
    "Class" : ["A","B","C","D","C"],
    "Score": [85, 55, 85, 82, 43],
    "Age": [15,12,53,12,16]
}
df = pd.DataFrame(data)

print("orignal Dataset :\n",df)

grouped = df.groupby("Class").mean()
print(grouped)

# calulate summary statics of group data
stats = df.groupby("Class").agg(
    {"Score":["mean","max","min"],"Age":["mean","max","min"]}
)
print(stats)
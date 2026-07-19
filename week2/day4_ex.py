import pandas as pd
import numpy as np

data = {
    "Name": ["Alice","Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 50],
    "Score": [85, 45, np.nan, 33]
    
}
import pandas as pd

# Calculate the minimum number of non-null values required to keep a column
# For 50% missing, we need at least 50% non-null values
threshold = len(data) * 0.50

# Drop columns exceeding the missing data limit
df_cleaned = data.dropna(thresh=threshold, axis=1)


df = pd.DataFrame(data)
# print("Original Dataset: \n",df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

# print("Dataset: \n",df)

df = df.rename(columns={"Name":"Student_Name"})
# print("Change in the column_name : \n",df)

df = df.dropna(axis =0)
# print("After drop missing  data in rows: \n",df)

# merging two datasets and perform data transformation

df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Alice", "Bob","Priya"],
    "Age": [23,45,12]
})

df2 = pd.DataFrame({
    "ID": [1,2,3],
    "Score": [45,67,93]
})

print("Dataser 1: \n",df1)
print("dataset 2: \n",df2)

merged = pd.merge(df1, df2, how="inner", on="ID")
print("merged Dataset: \n",merged)

merged["score_percentage"] = (merged["Score"]/100) *100
print("Transformed Dataset: \n",merged)
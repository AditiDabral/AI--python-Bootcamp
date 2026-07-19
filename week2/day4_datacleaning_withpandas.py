# data cleaning : clean data by filling missing value , droping missing value , interpolation, so that data can be ready to  used by pandas

import pandas as pd

# df = df.dropna() # drop missing values in rows
# df = df.dropna(axis=1) # rop missing values in columns

# df["column_name"] = df["column_name"].fillna(0)  # fill the missing values in particular column with 0

# # forward fill
# df.fillna(method="ffill") 
# #backward fill
# df.fillna(method="bfill") 

# df["column_name"] = df["column_name"].interpolate()  # fill by add similar data

 #data transformation: renaiming column , changing data type ,  creating & modifying column 
 
df = df.rename(columns ={"old_name": "new_name"})

df["coulmn_name"] = df["column_name"].astype("float")

df["colum_name"] = pd.to_datetime(df["column_name"]) # convert data type of column into date time

df["new_column"] = df["existing_coulmn"] * 2 # create a new column annd modify by existing column by mul 2 

# Combing and merging data frames : ex = u have data of diff years , u want to compare them or combine them by using : concatenation , Merging , Joining 

combined = pd.concat([df1 , df2], axis=0) # combing two data frames along  rows
combined = pd.concat([df1 , df2], axis=1) # combing two data frames(df1 &df2) along  column

merged = pd.merge(df1, df2 , on ="common_column")

merged2 = pd.merge(df1  , df2, how="left", on = "coomon_column")

merged2 = pd.merge(df1  , df2, how="inner", on = "coomon_column")

joined =  df1.join(df2 , how ="inner") # joing to data framed by indexing 
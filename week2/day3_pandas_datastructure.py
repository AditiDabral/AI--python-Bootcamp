# Pandas : python library for data manipulation and analysis ,provides fast and flexible data structures designed to work intuitively with structured, tabular data
import pandas as pd

# seeries : one dim data structure
s = pd.Series([1,2,3] ,index=["a","b","c"])
# print(s)

#data frame : 2 dim data structures like a table
data = {"Name":["Niha","Priya"],"Age":[12,34]}
df = pd.DataFrame(data)
# print(df)

## loading data from CSV , Excel , dict , other sources
# df = pd.read_excel("data.xlsx")
# df = pd.read_csv("data.csv")
# df.to_csv("data.csv",index = False)

# basic Dataframe operation : vie data , selecting  & indexing  

print(df.head()) #view data , print first 5 data set 
print(df.tail(4))  # print last 4 data set

print(df.info())  # provide compl info about head, column that uses some statics [summary of data frame]

print(df.describe())  # detailed statics summary [statistical summary of dataframe]

print(df["Name"])  #selecting colm
print(df[["Name","Age"]]) # give mul columns

print(df[df["Age"]>25]) #filtering

print(df.iloc[0]) # give first row by postion
print(df.iloc[:,0]) # give first column by postion
print(df.loc[0]) # give first row by index label
print(df.loc[:,"Name"]) # give name column
# grouping data in pandas
df = [4,5,6] # not orgin 
grouped = df.groupby("column_name")

# operation : Iterate over groups , applying aggregation

for name , group in grouped:
    print(name)
    print(group)

grouped.mean()
grouped.sum()

# aggregation function : using groupby , using pivot table , custom agg

#using group by
df.groupby("category_column") ["numeric_col"].mean()
df.groupby("category_column").age({"numeric_col": ["mean","max","min"]})

#using pivot_table

pivot = df.pivot_table(
    values = "numeric_col",
    index = "category_column",
    aggfunc ="mean"
)

#custom aggregration
def range_func(x):
    return x.max()- x.min()

df.groupby("category_column")["numeric_col"].age(range_func)


#calculating statics of grouped data : mean , max , min

    
df.groupby("category_column")["numeric_col"].mean()
df.groupby("category_column")["numeric_col"].max()
df.groupby("category_column")["numeric_col"].min()

# multi aggregation
df.groupby("category_column").agg(
    {"numeric_col":["mean", "max", "min"]}
)


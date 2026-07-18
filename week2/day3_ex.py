import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
)

#explore structure
print("first 5 rows :\n",df.head())
print("Last 2 rows :\n",df.tail(2))
print(df.describe())

# Select specific columns
selected_columns = df[["species", "sepal_length"]]
print(selected_columns)

# Filter rows
filtered_rows = df[
    (df["sepal_length"] > 5.0) &
    (df["species"] == "setosa")
]

print(filtered_rows)
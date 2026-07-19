import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

#Inspect Data
print(df.info())
print(df.describe())

# Handle missing values
# df["Age"] = df["Age"].fillna(df["Age"]).median()
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#Remove duplicates
df = df.drop_duplicates()

#filter data : Passenger in first class

first_class = df[df["Pclass"] == 1]
print("First Class passenger: \n",first_class.head())

# Generating Visualizaions to illustrate Key Insights

# bAR CHART OF SURVIVAL RATE BY CLASS
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind = "bar",color = "skyblue")

# plt.ylabel("Survival Rate")
# plt.title("Survival Rate by Class")
# plt.show()
plt.figure(figsize=(6,4))

sns.barplot(
    x=survival_by_class.index,
    y=survival_by_class.values
)

plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.title("Survival Rate by Passenger Class")
plt.tight_layout()
plt.show()

# Histogram for age distribution
sns.histplot(df["Age"],kde = True,bins= 20,color="purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# kind -->Specifies the type of graph (e.g., bar, line, pie, histogram)

# kde=True --> Adds a smooth density curve to show the data's distribution.

# bins=20 --> Divides histogram data into 20 intervals (bars).

# color --> Sets the color of the plot elements.

# figsize=(8,5)  --> Sets the width and height of the figure.

# xlabel()` --> Adds a label to the x-axis.

# ylabel() -->Adds a label to the y-axis.

# title() --> Adds a title to the graph.

# tight_layout() --> Automatically adjusts spacing so labels and titles don't overlap.

# show() -->Displays the graph on the screen.

#alpha controls the transparency (or opacity) of the plotted elements.
# alpha = 1 → Completely opaque (default).
# alpha = 0.5 → 50% transparent.
# alpha = 0 → Completely invisible.


# Scatter plot :Age Vs fare

# Small dots
# plt.scatter(df["Age"], df["Fare"], s=10)

# Larger dots
# plt.scatter(df["Age"], df["Fare"], s=100)

# Semi-transparent blue dots
plt.scatter(
    df["Age"],
    df["Fare"],
    s=15,
    color="green",
    alpha=0.6
)

plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare")
plt.show()

### Identify and Interpret Patterns or Anomalies

# Matplotlib for plotting data : python lib for creating statics, interactive , animated plots 

import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns


# x = [1,2,3,4]
# y =[10,20,30,40]
# plt.plot(x,y)
# plt.show()

# dif types of plot

#1. line plot

# plt.plot([1,2,3] ,[10,25,30], label = "Trend",color="green",linestyle= "--",marker ="o" ) # label will label the line name
# plt.title("Random line plot")
# plt.xlabel("This is x-axis")
# plt.ylabel("This is y-axis")
# plt.legend()
# plt.show()

#2.BAR chart

# categories = ["A","B","C"]
# values = [10,24,30]
# plt.bar(categories,values,color="pink")
# plt.title("Random bar chart")
# plt.show()

# 3. Histogram :show distibution od data structure

# data = [1, 2, 3,4 ,5 ,6 ,7,4,4,3]
# plt.hist(data, bins=4, color="purple", edgecolor="orange")
# plt.title("random Histogram")
# plt.show()

#4. scatter plot
# x = [1, 2, 3, 4, 5]
# y = [10,20,12,45,59]

# plt.scatter(x,y, color="red")
# plt.title("Random Scatter plot")
# plt.show()

# customizing plots : add titles, axis labels, legendss 2) adjust color and styles 

################# Seaborn :bulit on top of matplotlib for easier and more visually appleaing plots
# coomon seaborn plots : 1)heatmap : which viualizes a matrix of data | 2)pair plot: pair wise relationship with data

data = np.random.rand(5, 5)
sns.heatmap(data, annot=True,cmap="coolwarm")
plt.title("Random Heatmap")
plt.show()

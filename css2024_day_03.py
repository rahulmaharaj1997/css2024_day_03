#CSS2024 Python 
#Binyamin Barsch 

# EDA 

#import matplotlib.pyplot as plt

X = [0.5, 0.6, 0.7, 0.7,0.9] 
temp = [180, 200, 220, 240, 260] 

#plt.plot(temp, X) 
#plt.xlabel("temperature") 
#plt.ylabel("chemical conversion") 
#plt.title("Chemical Experiment") 
#plt.show() 

#import plotly.express as px 
#import webbrowser

#reac_conv = [0.5, 0.6, 0.7, 0.7,0.9] 
#temp = [180, 200, 220, 240, 260]  

#fig = px.line(x = temp , y= reac_conv) 

#fig.write_html("plot.html") 

#webbrowser.open("plot.html") 

import pandas as pd 
import matplotlib.pyplot as plt 

file = pd.read_csv("iris.csv") 

#Replacing the column name with 
#file["class"] = file["class"].str.replace("Iris")

#plt.scatter(file["sepal_length"],file["sepal_width"]) 
#plt.xlabel('sepal length') 
#plt.ylabel("sepal width")
#plt.show()

#plt.bar(file["class"],file["sepal_length"]) 
#plt.xlabel('sepal length') 
#plt.ylabel("sepal width")
#plt.show()

#df = pd.read_csv("time_series_data.csv")

#print(df.info())

#df["Date"] = pd.to_datetime(df["Date"], format= "%Y-%m-%d")

#df = pd.read_csv("poker_2016_09_27.csv") 

#col_names = [""]

#df["Time"] = pd.to_datetime(df["Time"], format="%H=%M-%S" ).dt.time 

#import pandas as pd
#from ydata_profiling import ProfileReport


import numpy as np 

x = np.arange(1,6) 

y = x**2 

print(np.matmul(x,y)) 

z = np.array(x,y) 
print("z=") 
print(y) 




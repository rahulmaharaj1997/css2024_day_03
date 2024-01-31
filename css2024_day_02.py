import pandas as pd




#df = pd.read_csv("patient_data_dates.csv", index_col=0)  
#df.drop(index=26, inplace=True) 

#ave_Cal = df["Calories"].sum() 
#df.fillna(ave_Cal, inplace=True)  
#df.dropna(inplace=True) 
#df["Duration"] = df["Duration"].replace([450],50) # Replace 450 in row 7 and column duration with 50
#print(df)

#df1 = pd.read_csv("person_split1.csv")  
#df2 = pd.read_csv("person_split2.csv")

#df3 = pd.read_csv("person_work.csv")  
#df4 = pd.read_csv("person_education.csv") 

#df.merge_inner = pd.merge(df1, df2, on="id")

import pandas as pd

#df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

#column_names = ["sepal length","sepal width","petal length", "petal width", "class"]

#df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=column_names, index_col=0)

#print(df)

#weather_data = pd.read_json("https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json",index_col=0) 
#print(weather_data)

#Data Frames
import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Adding a new column
#df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#print(df)

# Removing a column
#df.drop(columns=['new_column'], inplace=True)
#print(df)

# Displaying the DataFrame
# Creating a Frame 
#details = {"name":["Rahul", "Sanelisiwe", "Andy", "Sumesha", "Petricia", "Garcia"], 
 #          "age" : [26, 24,18, 33, 28, 26], 
 #          "gender" : ["M","F","M", "F", "F","F"]}  

# df = pd.DataFrame(details) 


#df["country"] = ["South Africa","Ghana", "USA","India","UK","UK"] 
#print(df)

#df.drop(columns=["age"], inplace=True) 
#print(df)

import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(df)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)




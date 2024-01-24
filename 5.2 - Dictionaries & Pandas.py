###########Dictionaries & Pandas


###########Dictionaries

#1/ Basics

d = {}

d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16

print(d["George"]) #print keys for

#keys are commonly strings or numbers
d[10] = 100

print(d[10])

#2/ Iteration through dictionary

# how to iterate over key-value pairs ?

for key, value in d.items():
    print("key:" + " " + str(key))
    print("value:" + " " + str(value))
    print("")

###########Pandas

#1 Reading Data - DataFrame

import pandas as pd

df = pd.read_csv("telco_churn.csv") #read csv file

tempdict = {"col1":[1,2,3],"col2":[4,5,6],"col3":[7,8,9] } #create a temp dictionary

dictdf = pd.DataFrame.from_dict(tempdict) #createDF from dictionary

Top_10_rows = df.head(10) #top 15 rows
Last_10_rows = df.tail(10) #lqst 15 rows

print(dictdf)

print(df.columns) # gives all the columns name

print(df.describe()) #gives high level statistic returns on these. Though this only works for integer or float type columns
print(df.describe(include ="object")) #gives high levle stats for "objects"

print(df.State) #filters and returns column state

print(df["State"]) #filters and returns column state (other way

print(df[["State", "International plan"]]) #filters and returns column state, International plan. Do it this way because call a column with a space in between

print(df.State.unique()) #returns only unique values of State column (take out doubles)

print(df[df["International plan"] == "No"])  #filter on columsn and rows where International plan = No

print(df[(df["International plan"] == "No") & (df["Churn"] == False)]) #filter on columsn and rows where International plan = No and Chrun = False

print(df[df["Churn"] == False])

print(df.iloc[14]) #grab 15th row
print(df.iloc[14,0]) #grab 15th row and column 1
print(df.iloc[22:33]) #slice of data from row 22 to row 32


#Setup Indexing on State
state = df.copy() #copy of our original df
state.set_index("State", inplace= True)

print(state.head())

print(state.loc["OH"])

#2 Updating Data - Data Frame

#Deleting Nulls
print(df.isnull().sum()) #will summ all the nulls per columns
df.dropna(inplace=True) #drop all rows with nothing inside
print(df.isnull().sum()) #check no more missing value

#Deleting Specific Column to DF
df.drop("Area code", axis = 1) #drops a column called "Area code"

#Adding New Column to DF
df["New Column"] = df["Total night minutes"] + df["Total intl minutes"] #adds New Columns at the end

print(df.columns)

df["New Column"] = 100 #update all values to 100

print(df.head())

df.iloc[0,-1] = 10 #updates just one vlaue

print(df.head())

#Condition based apply in DF
df["Churn Binary"] = df["Churn"].apply(lambda x: 1 if x == True else 0) #create a new column Churn Binary. Uses Lambda function to iterate thought elements and if Churn = "true" then input 1 else 0

print(df[df["Churn Binary"] == True].head()) #check if it works for Churn = True

#Ouptut

#CSV
df.to_csv("output.csv")

#json
df.to_json()

#html
df.to_html()

#delete
del df


#### Practice Excercises

#Dictionaries

#1 Basic

pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]

in_alb = countries.index("albania")
print(in_alb)
print(pop[in_alb])


world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
print(world["albania"])

#2 Pint out Keys

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe["norway"])


#3 Add and Delete key in dictionary

world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
world["sealand"] = 0.000028
print(world)
del(world["sealand"])

#4: working with Dictionaries
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe["france"]["capital"])

# Create sub-dictionary data
data = {"capital":"rome", "population":59.83}

# Add data to europe under key 'italy'
europe["italy"] = data

# Print europe
print(europe)

#####Pandas & Dataframes

#1: Basic

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country":names,"drives_right":dr,"cars_per_cap":cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

#2: Adding Row labels

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

#Ex3 import from CSV

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
#cars = pd.read_csv('cars.csv')    >>> import CSV
#cars = pd.read_csv('cars.csv', index_col = 0) >>>> import column

# Print out cars
print(cars)

#Ex4 Creating a Sub Data frame from Data Frame

# Import pandas as pd
import pandas as pd

# Print out cars
print(cars[["country"]]) #creating a sub data frame
print(cars[["country", "drives_right"]])
print(cars[1:3]) #row:column
print(cars[2:3]) #row:column


#Ex5: Row/Column access loc

# Import pandas as pd
import pandas as pd

#Row Access
print(cars.loc["RU"]) #selection based on index RU

#Row Access
print(cars.loc[["RU", "IN", "EG"]]) #Row Access

#Column Access
print(cars.loc[:,["country", "drives_right"]]) #column

#Rows & Column Access
print(cars.loc[["RU","IN"],["country", "drives_right"]]) #column

#Ex6: Row/Column access iloc

# Import pandas as pd
import pandas as pd

#LOC Row Access
print(cars.loc[["AUS","JPN","IN"]]) #selection based on index RU

#ILOC: Row Access
print(cars.iloc[[1,2,3]]) #selection wiht Iloc based on position

#LOC: Column Access
print(cars.loc[:,["country", "drives_right"]]) #column

#ILOC: Column Access
print(cars.iloc[:,[0,1]]) #column


#Ex6: Comparison


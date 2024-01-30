#####Netflix Project


#Step 1: creat list + dictionary
#Create a list of years from 2011 to 2020 and a list durations of the average movie lengths
# our friend provided (103, 101, 99, 100, 100, 95, 95, 96, 93, and 90).
#Create a dictionary movie_dict, with the keys "years" and "durations" and the
# values set to your lists years and durations.
#Print and inspect the dictionary to ensure it was created correctly.

years = list(range(2011,2021))
durations = (103, 101, 99, 100, 100, 95, 95, 96, 93,90)


print(len(years))
print(len(durations))

movie_dict = {"years": years, "durations": durations}
print(movie_dict)

#Step 2:
# Import pandas under its usual alias
import pandas as pd

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame.from_dict(movie_dict)


# Print the DataFrame
print(durations_df)

#Step 3:
# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure()

# Draw a line plot of release_years and durations
plt.plot(years,durations)


# Create a title
plt.title("Netflix Movie Durations")

# Show the plot
plt.show()

#step 4: read netflix

# Read in the CSV as a DataFrame
#cars = pd.read_csv('cars.csv')
##netflix_df = pd.read_csv("datasets/netflix_data.csv")


# Print the first five rows of the DataFrame
##print(netflix_df.iloc[:5])

#step 5

# Subset the DataFrame for type "Movie"
##netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
##netflix_movies_col_subset = netflix_df_movies_only[["title","country","genre","release_year","duration"]]

# Print the first five rows of the new DataFrame
##netflix_movies_col_subset.iloc[0:5]

#step 6: scatter plot

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
##x = netflix_movies_col_subset["release_year"]
##y = netflix_movies_col_subset["duration"]

##plt.scatter(x,y)

# Create a title
##plt.title("Movie Duration by Year of Release")

# Show the plot
##plt.show()

#step 7: Filter duration of 60min

# Filter for durations shorter than 60 minutes
##short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]
##print(short_movies[:5])

# Print the first 20 rows of short_movies
##print(short_movies[:20])


#8: Iterate through Panda and create a Colour list
# Define an empty list

colors = []

# Iterate over rows of netflix_movies_col_subset
##for col, row in netflix_movies_col_subset.iterrows():
##    if row["genre"] == "Children":
##        colors.append("red")
##    elif row["genre"] == "Documentaries":
##        colors.append("blue")
##    elif row["genre"] == "Stand-Up":
##        colors.append("green")
##    else:
##        colors.append("black")

# Inspect the first 10 values in your list
#print(colors[:10])


#9: Plotting with colors

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
##x = netflix_movies_col_subset["release_year"]
##y = netflix_movies_col_subset["duration"]

##plt.scatter(x,y,color = colors)

# Create a title and axis labels
##plt.title("Movie duration by year of release")
##plt.xlabel("Release Year")
##plt.ylabel("Duration (min)")

# Show the plot
##plt.show()
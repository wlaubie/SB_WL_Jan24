###########Dates & Time

######Datestime Module

#ex 1: Basics

import datetime

print((dir(datetime)))

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

mill = datetime.date(2000,1,1)
dt = datetime.timedelta(100)

print(mill + dt)

#ex 2: Day & time Format

print(gvr.strftime("%A, %B %d, %Y"))

#or

message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))


#ex 3: Date / Time / Date + Time

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22,27,0)
launch_datetime = datetime.datetime(2017, 3, 30, 22,27,0)

print(launch_date)
print(launch_time)
print(launch_datetime)
print((launch_datetime.year))


#ex 4: Date conversion from string

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")

print(moon_landing_datetime)


#ex 5: Date parsing

# Import pandas
import pandas as pd

# Load CSV into the rides variable
##rides = pd.read_csv('capital-onebike.csv',
##                    parse_dates = ["Start date", "End date"])   #parse_dat > parse_dates is enabled, pandas will attempt to infer the format of the datetime strings in the columns, and if it can be inferred, switch to a faster method of parsing them

##rides = pd.read_csv('capital-onebike.csv')

# Print the initial (0th) row
##print(rides.iloc[0])


#ex 6: Duration calculation

# Subtract the start date from the end date
##ride_durations = rides["End date"] - rides["Start date"]

# Convert the results to seconds
##rides["Duration"] = ride_durations.dt.total_seconds()

##print(rides['Duration'].head()) #The head() method returns a specified number of rows, string from the top. The head() method returns the first 5 rows if a number is not specified.



#ex 6: Summarizing Date Time in Panda

# on colum that make ses you can use stats calc.

#mean / median
##rides["duration"].mean()

#sum
##rides["duration"].sum()

#percent of time out of stock
##rides["Duration"].sum() / timedelta(days = 91)

#Count how many times the bike started at each station
##rides["member type"].value_counts()     ## returns a Series that contain counts of unique values

#percent of rides by member
##rides["Member type"].value_contents() / len(rides)

# Add duraiton (in seconds) column
##rides["Duraiton seconds"] = rides["Duration"].dt.total_seconds()







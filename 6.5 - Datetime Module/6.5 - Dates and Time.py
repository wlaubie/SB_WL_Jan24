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

#Average duration per member type

##rides.groupby("Member type")["Duration seconds"].means()

#Average duration by month

##rides.resample("M", on = "start date")["Duration seconds"].means()

#Size per group

##rides.groupby("member type").size()

# First ride per group

##rides.groupby("Member type").first()

# Plot results

##rides \
##    .resample("M", on = "start date")\
##    ["Duration seconds"]\
##    .mean()\
##    .plot()

#Ex 7: Joyrides

# Create joyrides
##joyrides = (rides['Start station'] == rides['End station'])

# Total number of joyrides
##print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
##print("The median duration overall was {:.2f} seconds"\
##      .format(rides['Duration'].median()))

# Median of joyrides
##print("The median duration for joyrides was {:.2f} seconds"\
##      .format(rides[joyrides]['Duration'].median()))

#Ex 8: Resample

# Import matplotlib
##import matplotlib.pyplot as plt

# Resample rides to daily, take the size, plot the results >> "D" for daily, "M" for monthly, etc
##rides.resample('D', on = 'Start date')\
##  .size()\
##  .plot(ylim = [0, 15])

# Show the results
##plt.show()


#Ex 9: Resample


# Resample rides to be monthly on the basis of Start date
##monthly_rides = rides.resample('M', on = "Start date")['Member type']

# Take the ratio of the .value_counts() over the total number of rides
##print(monthly_rides.value_counts() / monthly_rides.size())


#Ex 10: Median Duration wiht groupby

# Group rides by member type, and resample to the month
##grouped = rides.groupby('Member type')\
##  .resample('M', on = 'Start date')

# Print the median duration for each group
##print(grouped['Duration'].median())


#Ex 11: Timezone in Pandas with Localize

# Localize the Start date column to America/New_York
##rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')

# Print first value
##print(rides['Start date'].iloc[0])


#Ex 12: Timezone in Pandas with Converty (can only use localize once)

# Localize the Start date column to America/New_York
##rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')

# Print first value
##print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London
##rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')

# Print the new value
##print(rides['Start date'].iloc[0])


#Ex 13: Day name and groupby

# Add a column for the weekday of the start of the ride
##rides['Ride start weekday'] = rides['Start date'].dt.day_name()

# Print the median trip time per weekday
##print(rides.groupby('Ride start weekday')['Duration'].median())


#Ex 14: Final excercise

# Shift the index of the end date up one; now subract it from the start date
##rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
##rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
##monthly = rides.resample('M', on = "Start date")
##print(rides['Time since'])

# Print the average hours between rides each month
##print(monthly['Time since'].mean()/(60*60))
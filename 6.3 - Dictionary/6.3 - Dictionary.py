##### 6.3 - Dictionary

###Dictionary with CSV


#Ex 1: Reading CSV Data

import pandas as pd

Path = "Google Stock Market Data - google_stock_data.csv"

h = pd.read_csv("/Users/williamlaubie//Documents/GitHub/SB_WL_Jan24/6.3 - Dictionary/Google Stock Market Data - google_stock_data.csv")

Lines = [x for x in open(Path)] #read every line

print(Lines)
print(Lines[0])
print(Lines[1])

print(Lines[0].strip()) #delete white spaces
print(Lines[0].strip().split()) #delete white spaces + divide in smaller pieces

dataset = [x.strip().split(",") for x in open(Path)]

print(dataset) #will create a dataset with seperate values in each rows and columns

print(Lines[0])
print(Lines[1])


#Ex 2: Reading CSV Data

import csv
from datetime import datetime

path3 = "/Users/williamlaubie//Documents/GitHub/SB_WL_Jan24/6.3 - Dictionary/Google Stock Market Data - google_stock_data.csv"
file = open(path3,newline="")
reader = csv.reader(file)

header = next(reader) #first line is the header

print(header)

data = []

for row in reader:
    #[Date, Open, High, Low, Close, Volume, Adj Close]
    date = datetime.strptime(row[0],"%m/%d/%Y")
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close]) #create a tuple with data of every row in csv

print(data[0])

#Ex 3: compute + stroy daily reutnrs

return_path = "/Users/williamlaubie//Documents/GitHub/SB_WL_Jan24/6.3 - Dictionary/google_return.csv"
file = open(return_path,"w")
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    today_row = data[i]
    today_date = today_row[0]
    today_price = today_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (today_price - yesterdays_price)/ yesterdays_price
    formatted_date = today_date.strftime("%m/%d/%Y")
    writer.writerow([formatted_date,daily_return])


#Ex 4: Looping through tupples and dicitonaries

# Create an empty dictionary: squirrels_by_park
##squirrels_by_park = {}

# Loop over the squirrels list and unpack each tuple
##for park, squirrels_details in squirrels:
    # Add each squirrel_details to the squirrels_by_park dictionary
##    squirrels_by_park[park] = squirrels_details

# Sort the squirrels_by_park dict alphabetically by park
##for park in sorted((squirrels_by_park)):
    # Print each park and its value in squirrels_by_park
##    print(f'{park}: {squirrels_by_park[park]}')

#Ex 5: Get Keys from dictionary

# Safely print 'Union Square Park' from the squirrels_by_park dictionary
##print(squirrels_by_park.get("Union Square Park"))

# Safely print the type of 'Fort Tryon Park' from the squirrels_by_park dictionary
##print(type(squirrels_by_park.get('Fort Tryon Park')))

# Safely print 'Central Park' from the squirrels_by_park dictionary or 'Not Found'
##print(squirrels_by_park.get("Central Park", "Not Found"))


#6: Practice: Adding & extending Dictionaries

# Assign squirrels_madison as the value to the 'Madison Square Park' key
##squirrels_by_park['Madison Square Park'] = squirrels_madison

# Update squirrels_by_park with the squirrels_union tuple
##squirrels_by_park.update([squirrels_union])

# Loop over the park_name in the squirrels_by_park dictionary
##for park_name in squirrels_by_park:
    # Safely print a list of the primary_fur_color for each squirrel in park_name
##    print(park_name, [squirrel.get('primary_fur_color', 'N/A') for squirrel in squirrels_by_park[park_name]])


#7: Practice: Delete / Pop Dictionaries

# Remove "Madison Square Park" from squirrels_by_park and store it
##squirrels_madison = squirrels_by_park.pop("Madison Square Park")

# Safely remove "City Hall Park" from squirrels_by_park with an empty dictionary as the default
##squirrels_city_hall = squirrels_by_park.pop("City Hall Park", {})

# Delete "Union Square Park" from squirrels_by_park
##del squirrels_by_park["Union Square Park"]

# Print squirrels_by_park
##print(squirrels_by_park)

#8: Iterate over Dictionaries

# Iterate over the first squirrel entry in the Madison Square Park list
##for field, value in squirrels_by_park["Madison Square Park"][0].items():
    # Print field and value
##    print(field, value)

print('-' * 13)

# Iterate over the second squirrel entry in the Union Square Park list
##for field, value in squirrels_by_park["Union Square Park"][1].items():
    # Print field and value
##    print(field, value)

#9: Dictionary check if value is there

# Check to see if Tompkins Square Park is in squirrels_by_park
##if "Tompkins Square Park" in squirrels_by_park:
    # Print 'Found Tompkins Square Park'
##    print('Found Tompkins Square Park')

# Check to see if Central Park is in squirrels_by_park
##if "Central Park" in squirrels_by_park:
    # Print 'Found Central Park' if found
##    print('Found Central Park')

##else:
    # Print 'Central Park missing' if not found
##    print('Central Park missing')

#10: Dictiomnary keys and Iteration

# Print the keys from the squirrels_by_park dictionary for 'Union Square Park'
##print(squirrels_by_park["Union Square Park"].keys())

# Loop over the dictionary

##for park_name in squirrels_by_park:
    # Safely print the park_name and the highlights_in_fur_color or 'N/A'
    ##print(park_name, squirrels_by_park[park_name].get('highlights_in_fur_color', 'N/A'))


#11: Dictionary - list comprenhension and nested dictiomnaries

# Use a for loop to iterate over the squirrels in Tompkins Square Park:
##for squirrel in squirrels_by_park["Tompkins Square Park"]:
    # Safely print the activities of each squirrel or None
##    print(squirrel.get("activities"))

# Print the list of 'Cinnamon' primary_fur_color squirrels in Union Square Park
##print([squirrel for squirrel in squirrels_by_park["Union Square Park"] if "Cinnamon" in squirrel["primary_fur_color"]])
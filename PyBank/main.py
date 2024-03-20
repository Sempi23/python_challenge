import os
import csv

# path to collect data from the Resources Folder
budget_data.csv = os.path.join("...", "Resources", "budget_data.csv")

# Open and read csv
with open(budget_data,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"header: {csv_header}")

# define the funciton and have it accept the 'budget_data' as its sole parameter
    date = []
    month = str(date[0])
    profit = []

# calculate total number of months in the dataset
    for row in csvreader:
        count = count + 1

        date.append(row[1])
        month.append (row[0])

    
# Net total profit or loss for entire period
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
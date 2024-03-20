import os
import csv

# path to collect data from the Resources Folder
budget_data = os.path.join("Resources", "budget_data.csv")

# Initialize variables
count_months = 0
total_profit = 0

# Create empty lists to iterate through specific rows
monthly_profit_change = []
total_months = []
greatest_increase = ["",0]
greatest_decrease = ["", 10000000]


# Open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"header: {csv_header}")

      
# calculate total number of months in the dataset
    # Loop through to find total months
    for rows in csvreader:
        count_months = count_months + 1
        total_profit += int(rows[1]) 
        print(count_months)
        #print(int(rows[1]))
        
# Append the total months & total profit to their correstponding lists
    #total_months.append(rows[0])
        monthly_profit_change.append(int(rows[1]))    
   
    
# Net total profit or loss for entire period
     # Loop through rows in the csv file 
    #for rows in csvreader:
        #count_months += 1
       # total_profit += int(row[1])   
       # total_profit = sum(int(rows[1]))
       # print(total_profit)

# Changes in profit/losses over the entire period
    monthly_profit_change = []
# Average of the profit/loss changes
    average (montly_profit_change)

# Greatest increase in profits(date & amount) over the entire period
        #greatest_increase = max(montly_profit-Change)
    

# Greatest decrease in profit (date & amount) over the entire period
        #greatest_decrease = min(monthly_profit_change)

# Analysis results
    
# Print("Financial Analysis")

print("------------------------------")

print(f"Total Months: {count_months}")

print(f"Total profit: {total_profit}")
    
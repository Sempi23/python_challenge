import os
import csv

# path to collect csv data from the Resources folder
#budget_data = os.path.join('Resources', 'budget_data.csv')

file_to_load = "PyBank/Resources/budget_data.csv"

# Output path
file_to_output = "PyBank/analysis.budget_analysis.txt"

# Open and read the csv file
#with open(budget_data, newline="") as csvfile:
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip header row 
    csv_header = next(csvreader)


# initialize variables
    total_months = 0
    net_total = 0
    average_change = 0
    previous_profit_loss = 0
    monthly_changes = []
    greatest_increase = 0
    greatest_decrease = 0
    greatest_decrease_date = []
    greatest_increase_date = []

# Loop through rows in the csv
    for row in csvreader:
    
    # calculate total number of months in the dataset
        total_months += 1

    # calculate net total profit or loss for entire period
        net_total += int(row[1])

    # calculate changes in profit/losses over the entire period
    if previous_profit_loss != 0:
        monthly_change = int(row[1]) - previous_profit_loss
        monthly_changes.append(monthly_change)

    # update previous_profit_loss for the next iteration
        previous_profit_loss = int(row[1])

# calculate the average profit/loss change
if len(monthly_changes) > 0:  
    average_change = sum(monthly_changes) / len(monthly_changes)

# calculate greatest increase in profit/loss(date & amount)  over the entire period
    greatest_increase = max(monthly_changes)

# calculate greatest decrease in profit (date & amount) over the entire period
    greatest_decrease = min(monthly_changes)

# find corresponding date for the greatest increase and decrease
    greatest_increase_date = row[monthly_changes.index(greatest_increase)]
    greatest_decrease_date = row[monthly_changes.index(greatest_decrease)]
    
# Print Analysis results

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date[0]} (${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_date[0]} (${greatest_decrease}")

# write analysis results to a text file 
#with open(file_to_output, "w") as txtfile:
    #txtfile.write(output)


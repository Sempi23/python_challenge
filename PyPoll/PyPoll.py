import os
import csv

# path to collect data from the Resources Folder
election_data = os.path.join("Resources", "election_data.csv")

# Open and read csv file
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile) # Skip the header row
    print(f"Header: {csv_header}")

# Declare variables
    total_votes = 0
    winner_count = 0
    candidates = {}
    #Charles Casper Stockham


    # Find the total number of votes cast
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates.keys():
          print(row[2])     
         # print(f"Total Votes: {total_votes}")
          
       

# Creat a complete list of candidates who received votes
    
# Calculate percentage of votes each cadidate won
    
# Calculate the total number of votes each candidate won
    
# Determine the winner of the election based on popular vote



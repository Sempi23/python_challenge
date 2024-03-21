import os
import csv

# path to collect data from the Resources Folder
election_data = os.path.join("Resources", "election_data.csv")

# Open and read csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) # Skip the header row
    #print(f"Header: {csv_header}")

# Declare variables
    total_votes = 0
    winner_count = 0
    Stockham_votes = 0
    DeGette_votes = 0
    Doane_votes = 0
    candidates = []
    votes = []
    candidate_votes = {} # dictionary to store votes for each candidate
    

# Find the total number of votes cast
    for row in csvreader:
        total_votes = total_votes + 1 
        candidate = row[2]

       # if candidate in candidate_votes:
            #candidate_votes[candidate] += 1
        #else:
            #candidate_votes[candidate] = 1

        #print(f"Total Votes: {total_votes}")
        #print("Total Votes per Candidate:")
        #for candidate, votes in candidate_votes.items():
            #print(f"{candidate}: {votes}")
           

# Create a complete list of candidates who received votes
       # if row[2] == "Charles Casper Stockham":
            #Stockham_votes +=1
       # elif row[2] == "DeGette":
            #DeGette_votes +=1
        #elif row[2] == "Doane":
            #Doane_votes +=1

        #print(f"Stockham votes: {Stockham_votes}")

# Calculate percentage of votes each cadidate won
    for candidate, votes in candidate_votes.items():
        percent = (votes /total_votes) * 100.0
        print(f"{candidate} Percentage: {percent}")
#Stockham_percent = (Stockham_votes / total_votes) * 100
#DeGette_percent = (DeGette_votes / total_votes) * 100
#Doane_percent = (Doane_votes / total_votes) * 100

#print(f"Stockham Percentage: {Stockham_percent}")
#print(f"DeGette Percentage: {DeGette_percent}")
#print(f"Doane Percentage: {Doane_percent}")           
    
# Calculate the total number of votes each candidate won
    #make a dictionary out of the two lists
       # candidates = ["Stockhom", "DeGette", "Doane"]
        #votes = ["stochom_votes", "DeGette_votes", "Doane_votes"]
    # Zip the two lists together with candidate as key and total_votes as value
            #dict_candidates_and_votes =dict(zip(candidates, votes))
            #key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)
    
# Determine the winner of the election based on popular vote
        
# Analysis Results
        #print(f"Election Results\n")
        #print(f"--------------------------\n")
        #print(f"Total Votes: {total_votes}\n")
        #print(f"--------------------------\n")



import os
import csv

# path to collect data from the Resources Folder
election_data = os.path.join("Resources", "election_data.csv")

# Output file
file_to_output = "Analysis/election-analysis_txt"

# Open and read csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) # skip header row
    
# Declare variables
    total_votes = 0
    candidate_list = []
    votes = []
    candidate_and_votes = {} # dictionary to store votes for each candidate
    percentages = {} # dictionary to store percentage of votes for each candidate
    

# Find the total number of votes cast
    for row in csvreader:
        total_votes += 1 

    #collect candidates and their votes
        candidate = row[2]
        if candidate not in candidate_and_votes:
                candidate_and_votes[candidate] = 0
        candidate_and_votes[candidate] += 1
        
#calculate the percentage of votes each candidate won
    for candidate,votes  in candidate_and_votes.items():
        percent_votes = (votes / total_votes)  * 100
        percentages[candidate] = (candidate_and_votes[candidate] / total_votes) * 100
        #print(f"{candidate} percentage: {percent_votes:.3f}%")

# Determine the winner of the election based on popular vote
        winner = max(candidate_and_votes, key=candidate_and_votes.get)
    #print(f"winner: {winner}")
        
# Analysis summary table
print(f"Election Results\n")
print(f"--------------------------\n")
print(f"Total Votes: {total_votes}\n")
print(f"--------------------------\n")
for candidate, votes in candidate_and_votes.items():
    print(f"{candidate}:  {percentages[candidate]:.3f}% ({votes})")

print(f"--------------------------\n")
print(f"Winner: {winner}\n")
print(f"--------------------------\n")

# write output to analysis folder
with open(file_to_output, "w") as txtfile:
        
    txtfile.write(f"Election Results\n")
    txtfile.write(f"--------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"--------------------------\n")
    for candidate, votes in candidate_and_votes.items():
            txtfile.write(f"{candidate}: {percentages[candidate]:.3f}%({votes})\n")

    txtfile.write(f"--------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"--------------------------\n")




import csv
from pathlib import Path

#data_folder = Path("PyPoll/Resources/")
#file_to_open = data_folder / "election_data.csv"

election_csv = Path("PyPoll/Resources/election_data.csv")
#print(election_csv.name)


# Initialize Variables 
total_votes = 0
candidate_votes = {}


#Read csv file
with open(election_csv,'r') as file:
    reader= csv.DictReader(file)
    
    # Iterate through each row in the dataset
    for row in reader:
        total_votes += 1
        candidate = row['Candidate']
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate]= 1

# Calculate percentages and determine the winner
winner = None
winner_votes = 0

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_votes[candidate] = (votes, percentage)
    
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate




# Print the total number of votes cast
print(f"Total Votes: {total_votes}")
print(candidate_votes)
for candidate, (votes, percentage) in candidate_votes.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print(f"Winner: {winner}")
    
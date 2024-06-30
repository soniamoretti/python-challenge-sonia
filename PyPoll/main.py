import csv
from pathlib import Path


election_csv = Path("PyPoll/Resources/election_data.csv")
#print(election_csv.name)

output_directory = Path('PyPoll/Analysis')
# Ensure the directory exists
if not output_directory.exists():
    output_directory.mkdir(parents=True, exist_ok=True)
output_file_path = output_directory / 'election_analysis.txt'


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


# Print results
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
for candidate, (votes, percentage) in candidate_votes.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")


# Export the analysis results to a text file
with output_file_path.open('w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("-------------------------\n")
    for candidate, (votes, percentage) in candidate_votes.items():
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
    
print("Analysis results exported to election_analysis.txt")
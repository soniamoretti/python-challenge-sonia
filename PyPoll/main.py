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

# Print the total number of votes cast
print(f"Total Votes: {total_votes}")
print(candidate_votes)
    
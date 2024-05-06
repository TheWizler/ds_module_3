import csv
import os

# Path
file_path = 'PyPoll/Resources/election_data.csv'

# Create the Analysis folder if it doesn't exist
output_folder = 'Analysis'
os.makedirs(output_folder, exist_ok=True)

# Variables
total_votes = 0
candidates = {}

# Open and read CSV
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    # Process each row
    for row in reader:
        total_votes += 1
        candidate_name = row[2]  # Candidate names

        # If the candidate is already in the dictionary, increase incrementally
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            # Otherwise, add the candidate to the dictionary with one vote
            candidates[candidate_name] = 1

# Determine winner and output
winner = None
max_votes = 0
output = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]

for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    output.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

output += [
    "-------------------------",
    f"Winner: {winner}",
    "-------------------------"
]

# Define the output file path within the Analysis folder
output_file_path = os.path.join(output_folder, 'election_results.txt')

# Print the output to the terminal
for line in output:
    print(line)

# Write the output to the text file in the Analysis folder
with open(output_file_path, 'w') as output_file:
    for line in output:
        output_file.write(line + '\n')

import os
import csv

# Get the current working directory
current_dir = os.getcwd()

# Specify the relative path to the 'election_data.csv' file
election_data = os.path.join(current_dir, "PyPoll", "Resources", "election_data.csv")

# A list to capture the names of candidates
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    for votes in num_votes:
        percentage = (votes / total_votes) * 100
        percentage = round(percentage, 3)
        percentage = f"{percentage:.3f}%"
        percent_votes.append(percentage)

    winner_votes = max(num_votes)
    winner_index = num_votes.index(winner_votes)
    winning_candidate = candidates[winner_index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_votes[i]} ({num_votes[i]})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output_path = os.path.join(current_dir, "PyPoll", "output.txt")
with open(output_path, "w") as output:
    output.write("Election Results\n")
    output.write("--------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("--------------------------\n")
    for i in range(len(candidates)):
        output.write(f"{candidates[i]}: {percent_votes[i]} ({num_votes[i]})\n")
    output.write("--------------------------\n")
    output.write(f"Winner: {winning_candidate}\n")
    output.write("--------------------------\n")
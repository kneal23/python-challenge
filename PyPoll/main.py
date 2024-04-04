#First import packages to be used
import os
import csv

poll_data = os.path.join('/Users/keshia/Desktop/Bootcamp Challenges/python-challenge/PyPoll','Resources',
                           'election_data.csv')

with open (poll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        print(row)

#The total number of votes cast
votes = []

with open (poll_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    for row in csv_reader:      
        votes.append(row[2]) 
print(f"Total Votes:" + str(len(votes)))




#A complete list of candidates who received votes and totals
  #Create a dictionary of canddiate names
candidate_votes = {
    "Charles Casper Stockham": 0,
    "Diana DeGette": 0,
    "Raymon Anthony Doane": 0}

# Read the CSV file and update vote counts for each candidate
with open(poll_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip the header row

    # Update vote counts for each candidate
    for row in csv_reader:
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1

# Print individual totals for each candidate
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes}")




#The percentage of votes each candidate won
 #Create a dictionary of canddiate names
candidate_votes = {
    "Charles Casper Stockham": 0,
    "Diana DeGette": 0,
    "Raymon Anthony Doane": 0}

# Read the CSV file and update vote counts for each candidate
total_votes = 0
with open(poll_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip the header row

    # Update vote counts for each candidate
    for row in csv_reader:
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
            total_votes += 1

# Calculate and print percentages for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}%")




#The winner of the election based on popular vote
# Initialize a dictionary to store the candidates and their vote counts
candidate_votes = {
    "Charles Casper Stockham": 0,
    "Diana DeGette": 0,
    "Raymon Anthony Doane": 0
}

# Read the CSV file and update vote counts for each candidate
total_votes = 0
with open(poll_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip the header row

    # Update vote counts for each candidate
    for row in csv_reader:
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
            total_votes += 1

# Determine the winner based on popular vote
winner = ""
max_votes = 0
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Determine the message based on whether the winner received more than 50% of the votes
if max_votes / total_votes > 0.5:
    message = "Candidate received the most votes"
else:
    message = "Candidate did not receive enough votes"

# Print the winner and the message
print(f"{winner} {message}")
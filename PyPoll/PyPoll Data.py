import os
import csv

election_data_csv = os.path.join("PyPoll/Resources/election_data.csv")

total_votes = 0
candidate_votes = {}
candidates = []

with open(election_data_csv) as csvfile:
    cvsreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(cvsreader)

    for row in cvsreader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] += 1


candidate_percent = {}
for candidate in candidates:
    votes = candidate_votes[candidate]
    percent = (votes/total_votes) * 100
    candidate_percent[candidate] = percent

winner = max(candidate_votes, key = candidate_votes.get)


print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

for candidate in candidates:
    print(f"{candidate}: {candidate_percent[candidate]:.3f}% ({candidate_votes[candidate]})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

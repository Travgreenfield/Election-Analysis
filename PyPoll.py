#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote

import csv
import os

#Assigning a variabel for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Creating a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Variable for the accumulator and initialize the total vote counter
total_votes = 0

# Declaring a variable for the candidate list
candidate_options = []

# Creating an empty dictionary to assign the candidate as the key and a single vote as a value
candidate_votes = {}

# Creating a variable for the winning candidate
winning_candidate = ""
# Variable for Winning Count
winning_count = 0
# Variable for Winning Percentage
winning_percentage = 0
with open(file_to_load) as election_data:
    #To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    #Print header row
    headers = next(file_reader)
    
    # Iterate through each row in the CSV file
    for row in file_reader:
        total_votes += 1

        # Iterating through to get the candidates for candidate list
        candidate_name = row[2]

        # Add the candidate name to the candidate list created at the start
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking the number of votes
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    # Creating variable for percentage of votes awarded
    vote_percentage = (int(votes) / int(total_votes)) * 100

    print(f"{candidate}: {vote_percentage:.1f}% ({votes})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage

        winning_candidate = candidate

winning_candidate_summary = (
    f"--------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"WInning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------------\n")
print(winning_candidate_summary)

# Using the open() function with the "w" mode we will write data to the file
#with open(file_to_save, "w") as txt_file:
    #txt_file.write('Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson')


# Required directives
import csv
import os

# Setting variables
# CSV file to pull from
file_to_load = 'Resources/election_results.csv'
# Text file to save to
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Variable for the accumulator and initialize the total vote counter
total_votes = 0

# Variable for the county accumulator and initialize the county vote counter
county_total = 0

# Declaring a variable for the candidate list
candidate_options = []
# Creating an empty dictionary to assign the candidate as the key and a single vote as a value
candidate_votes = {}

# Declaring a variable for the county list
county_options = []
# Creating an empty dictionary to assign the county as the key and a single vote as a value
county_votes = {}

# Creating a variable for the winning candidate
winning_candidate = ""
# Variable for Winning Count
winning_count = 0
# Variable for Winning Percentage
winning_percentage = 0

# Creating a variable for the winning county
winning_county = ""
# Creating a variable for winning county vote 
winning_turnout = 0
# Creating a variable for winning county percentage
county_winning_percentage = 0

with open(file_to_load) as election_data:
    #To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    #Skip header row
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

        county_name = row[1]

        if county_name not in county_options:
            county_options.append(county_name)
            #begin tracking the number of county votes
            county_votes[county_name] = 0

        county_votes[county_name] += 1

# Accessing file to write into
with open(file_to_save, "w") as txt_file:   
    
    #printout formatting
    format_shell = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n"
        f"\n")
    print(format_shell)
    txt_file.write(format_shell)

    #printout formatting
    print("County Votes:\n")
    txt_file.write("County Votes:\n")

    # Iterate through each value in the county votes dictionary
    for county in county_votes:
        turnout = county_votes[county]
        # Creating variable for percentage of votes per county
        turnout_percentage = (int(turnout) / int(total_votes)) * 100

        # Designating county vote, winner, and winning percentage data
        if (turnout > winning_turnout) and (turnout_percentage > county_winning_percentage):
            winning_turnout = turnout
            county_winning_percentage = turnout_percentage

            winning_county = county

        #Printing iterated results
        county_results = (f"{county}: {turnout_percentage:.1f}% ({turnout:,})")
        print(f"{county_results}\n")
        txt_file.write(f"{county_results}\n")

    #Printing singular results
    print(
        f"\n"
        f"--------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"--------------------------\n"
    )
    txt_file.write(
        f"\n"
        f"--------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"--------------------------\n"
    )        

    # Iterate through each value in the candidates votes dictionary
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        # Creating variable for percentage of votes awarded
        vote_percentage = (int(votes) / int(total_votes)) * 100

        # Designating candidate vote, winner, and winning percentage data
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage

            winning_candidate = candidate
        
        #Printing iterated results
        candidate_results = (f'{candidate}: {vote_percentage:.1f}% ({votes:,})')
        print(
            f"{candidate_results}\n"
        )
        txt_file.write(
            f"{candidate_results}\n"
        )
    #Printing singular results
    print(
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------"
        )
    txt_file.write(
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------"
        )    
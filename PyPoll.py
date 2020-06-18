#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote

import csv
dir(csv)
dir(int)
import os

#Assigning a variabel for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Creating a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    #To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    #Print header row
    headers = next(file_reader)
    print(headers)

    


# Using the open() function with the "w" mode we will write data to the file
#with open(file_to_save, "w") as txt_file:
    #txt_file.write('Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson')


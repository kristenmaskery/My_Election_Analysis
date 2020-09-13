# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
county_turnout = ""
voter_count = 0 

# Read the csv and convert it into a list of dictionaries
with open("election_results.csv") as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1


# Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")
        txt_file.write(election_results)


    # 6a: Write a repetition statement to get the county from the county dictionary.
        for county_name in county_votes:
        # 6b: Retrieve the county vote count.
            c_votes = county_votes[county_name]

        # 6c: Calculate the percent of total votes for the county.
            vote_percentage = float(c_votes) / float(total_votes)* 100

         # 6d: Print the county results to the terminal.
            county_results =(
            f"{county_name}: {vote_percentage:.1f}% ({c_votes:,})\n")
            print(county_results)
            txt_file.write(county_results)
         # 6e: Save the county votes to a text file.
         # 6f: Write a decision statement to determine the winning county and get its vote count.
            if (c_votes > voter_count): 
                voter_count = c_votes
                county_turnout = county_name
        winning_county_summary = (
            f"----------------------------\n"
            f"Largest County Turnout: {county_turnout}\n"
            f"-----------------------------\n")
        print(winning_county_summary)
        txt_file.write(winning_county_summary)

    # 7: Print the county with the largest turnout to the terminal.


    # 8: Save the county with the largest turnout to a text file.
    

     #1. Iterate through the candidate list
        for candidate_name in candidate_votes:
            #2. Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #3. Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes)* 100
             #print(winning_candidate_summary)
            #Create candidate results variable
            candidate_results = (
                 f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #Print each candidate, their vote count, and percentage to the terminall
            print(candidate_results)
            # Save the candidate results to our text file
            txt_file.write(candidate_results)
            
        
            #Determie winning vote count and candidate
            #1. Determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #2. if true then set winning_count=votes and winning_percentage= vote_percenntage
                winning_count = votes
                winning_percentage = vote_percentage
                #3. set the winning candidate equal to candidate's name
                winning_candidate = candidate_name
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        #Save the winning candidate's results to the text file
        txt_file.write(winning_candidate_summary)
       

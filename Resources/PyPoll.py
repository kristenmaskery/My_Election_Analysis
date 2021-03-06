# Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initialize a total vote counter
total_votes = 0

#Candidate Options
candidate_options = []
#1. Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open("election_results.csv") as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        #2 Add to the total vote count
        total_votes += 1 
        #Print the candidate name for each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's vote count
        candidate_votes[candidate_name] +=1
        
    #Save the results to our text file
    with open(file_to_save,"w") as txt_file:
        #Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the txt file
        txt_file.write(election_results)
            

        #Determine the percentage of votes for each candidate by looping through the counts
        #1. Iterate through the caandidate list
        for candidate_name in candidate_votes:
            #2. Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #3. Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes)* 100
             #print(winning_candidate_summary)
            #Create candidate results variable
            candidate_results = (
                 f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}\n")
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

   







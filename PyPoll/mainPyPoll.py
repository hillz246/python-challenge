import os
import csv

election_data = os.path.join('Resources', "election_data.csv")

# A list to capture the names of candidates
candidts = []

# A list to capture the number of votes each candidate receives
num_vts = []

# A list to capture the percentage of total votes each candidate 
percent_vts = []

# A count for the total number of votes 
total_vts = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        total_vts += 1 

        #        If the candidate is not on our list, add his/her name to our list, along with a vote in his/her name.If he/she is already on our list, we will simply add a vote in his/her name 
        
        if row[2] not in candidts:
            candidts.append(row[2])
            index = candidts.index(row[2])
            num_vts.append(1)
        else:
            index = candidts.index(row[2])
            num_vts[index] += 1
    
    # Add to percent_vts list 
    for vts in num_vts:
        percentage = (vts/total_vts) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_vts.append(percentage)
    
    # Find the winning candidate
    winner = max(num_vts)
    index = num_vts.index(winner)
    winning_candidate = candidts[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_vts)}")
print("--------------------------")
for i in range(len(candidts)):
    print(f"{candidts[i]}: {str(percent_vts[i])} ({str(num_vts[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_vts)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidts)):
    line = str(f"{candidts[i]}: {str(percent_vts[i])} ({str(num_vts[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
import os 
import csv

file_path = "Resources/election_data.csv"

election_data = {}
winner = ""  
winnervotes = 0

#open file path as read, assign delimiter of the file as comma and skip the header. 
with open(file_path, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    
#find non existant values in column 2 and add them to empty dictinary called election_data 
    for row in csvreader: 
        candidate=row[2]        
        if candidate not in election_data:
            election_data[candidate] = 0 
        #look through all the values and add 1 tick for every unique value read
        election_data[candidate] += 1
#create two new variales, one to store the number of votes and another the winner, sort through the data and add
#every tick (unique count) to winnervotes, while comparing values for every candidate.  
        if election_data[candidate] > winnervotes: 
            winnervotes = election_data[candidate]  
            winner = candidate


#print all values statements 
print("Election Results")
print("------------------------")
print("Total Votes",sum(election_data.values()))
print("------------------------")
print(election_data)
print("------------------------")
print("Winner:", winner)
print("------------------------")

output_path = os.path.join( "analysis", "output.txt")
with open(output_path, 'w') as csvfile: 

# Initialize csv.writer.
    csvwriter = csv.writer(csvfile, delimiter=':')

    # Add all output values to a CSV file. 
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(["Total Votes", sum(election_data.values())])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow([election_data])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(["Winner:",winner])
    csvwriter.writerow(['------------------'])





    


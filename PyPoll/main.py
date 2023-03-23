import os 
import csv

file_path = "Resources/election_data.csv"

election_data = {}
winner = ""  
winnervotes = 0


with open(file_path, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    

    for row in csvreader: 
        candidate=row[2]
        if candidate not in election_data:
            election_data[candidate] = 0 

        election_data[candidate] += 1

        if election_data[candidate] > winnervotes: 
            winnervotes = election_data[candidate]  
            winner = candidate



print("Election Results")
print("------------------------")
print("Total Votes",sum(election_data.values()))
print("------------------------")
print(election_data)
print("------------------------")
# print(election_data.keys())
# print(election_data.values())
print(winner, winnervotes)
print("------------------------")







    


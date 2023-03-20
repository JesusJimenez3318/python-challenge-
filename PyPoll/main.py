import os 
import csv

file_path = "Resources/election_data.csv"

ballot_id =[]
county = []
candidate = [] 
newcandidate = []

with open(file_path, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
   
    
#create 3 variables that contain the location of the data you want to add to your dictonary 

    for row in csvreader: 
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    election_data = {} 
    election_data = {"ballot_id": ballot_id,"county":county,"candidate":candidate} 
    
    totalvotes = len(ballot_id)

    for value in candidate:
        if value not in newcandidate: 
            newcandidate.append(value)
    print(newcandidate)





    

    # for votes in candidate:
    #     if votes not in newcandidate:
    #         candidate[votes] = 0
    #     election_data[votes] = election_data[votes] + 1

    #final_list = [{'num' : votes, 'count': election_data[votes]} for votes in election_data]


#print(final_list)
print(totalvotes)


    
   





# A complete list of candidates who received votes





# The percentage of votes each candidate won





# The total number of votes each candidate won





# The winner of the election based on popular vote

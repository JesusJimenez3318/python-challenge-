import os
import csv 

file_path = "C:/Users/JJ/Documents/Data BC/Asignments/python-challenge-/PyBank/Resources/budget_data.csv"

date=[] 
budget=[]
total = 0
diff2 = 0
max = 0
min = 0
count = 0

#open a path and mark ir as read
with open(file_path,mode = 'r') as csvfile: 

    #tell python the file is comma separated and make a variable to ignore the header
    csvreader  = csv.reader(csvfile,delimiter = ',') 
    cvsheader = next(csvreader)
    for row in csvreader:
        #assign the values to the created libraries. 
        date.append(row[0])
        budget.append(row[1])

 #sum the total profit/loss (row 1)   
for x in range(0, len(budget)):
    total = total + int(budget[x])

#in row 1, asign range in the sum of the subget values

for y in range(1,len(budget)): 
    #crete variables to compare two different values, and look at the
    #differentiate between them,(max and min), read through the row, and 
    #assign the value found. 
    diff = (int(budget[y])-int(budget[y-1]))
    diff2 = diff + diff2  
    #is the current value bigger than the  value max?
    if diff > max: 
        max = diff 
        maxmonth = str(date[y])
    #is the current value lower than  min?
    elif diff < min:
        min = diff
        minmonth = str(date[y]) 
    #create a counter for for all the values look trough 
    count = count + 1
    #calculate the average 
    diff3 = round(diff2/count, 2)

#print all of the values
print('Financial Analysis')
print('-----------------------')
print(len(date))#print sum of values in library (row 0)
print(total)
print(diff3)
print(maxmonth, max)
print(minmonth, min)

# Specify where the file is going to be writen
output_path = os.path.join( "analysis", "output.txt")

# Open the file using "write" mode
with open(output_path, 'w') as csvfile: 

# Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=':')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Total', len(date)])
    csvwriter.writerow(['Total', total,])
    csvwriter.writerow(['Average Change', diff3])
    csvwriter.writerow(['Greatest Increase in Profits', maxmonth," ", max])
    csvwriter.writerow(['Greatest Decrease in Profits', minmonth,"", min])
    csvwriter.writerow(['------------------'])


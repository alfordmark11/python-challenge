import os
import csv

# variables 
months = []
profit = []
average_change = 0
total_months = 0
net_change = []



#open the csv file and set delimiter
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header row
    csv_header = next(csvreader)



    #create a loop to read through the data 
    for row in csvreader:
        month = row[0]
        months.append(month)
        values = int(row[1])
        profit.append(values)

total_months = len(months)
total_Profits = sum(profit)
nettotalmonths = len(months) - 1
differenceData = []

for value in range(len(profit) - 1):
    differenceData.append(float(profit[value +1]) - float(profit[value]))
    newnettotal = sum(differenceData)

averagechange = newnettotal/nettotalmonths

greatest_loss = profit[profit.index(min(profit))] - profit[profit.index(min(profit)) - 1]
greatest_gain = profit[profit.index(max(profit))] - profit[profit.index(max(profit)) - 1] 

#print the results
print(f"Total Months: {total_months}")
print(f"Total: ${total_Profits}")
print(f"Average Change: ${round(averagechange,2)}")
print(f"Greatest Increase in Profits: {months[profit.index(max(profit))]} (${greatest_gain})")
print(f"Greatest Decrease in Profits: {months[profit.index(min(profit))]} (${greatest_loss})")

#creat a file with created data
output = "Analysis_Data.txt"
with open(output, "w") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Analysis"])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${total_Profits}"])
    csvwriter.writerow([f"Average Change: ${round(averagechange,2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {months[profit.index(max(profit))]} (${greatest_gain})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {months[profit.index(min(profit))]} (${greatest_loss})"])

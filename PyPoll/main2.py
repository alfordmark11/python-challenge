
import os
import csv
#set a variable for the total votes
totalvotes = 0
Candidatelist = []
CandiateDictionary = {}
votespercandidate = 0
winner = ""
#open the csv file and set delimiter
with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip the header
    csv_header = next(csvreader)

    for row in csvreader:
        #start counting votes
        totalvotes += 1
        # see who the vote was for 
        candidate = row[2]

        # create an if statement to assign the vote to the proper canidate
        if candidate not in  Candidatelist:
            #we have to add the canidate to the canidate list 
            Candidatelist.append(candidate)
            #set the new candidate vote total to zero
            CandiateDictionary[candidate] = 0
        #add the vote to the the candidate who is in the dictionary
        CandiateDictionary[candidate] += 1

#print results of total votes 
print(f"Total Votes: {totalvotes}")

#create an output file
outputfile = "Election Results.txt"
with open(outputfile, "w",) as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow([f"Election Results"])
    csvwriter.writerow([f"-------------------"])
    csvwriter.writerow([f"Total Votes: {totalvotes}"])
    csvwriter.writerow([f"-------------------"])
    # to calculate the percent of votes loop through the candidate dict.
    for candidate in CandiateDictionary:
        # variable to hold each candidates vote percentage 
        percentage = round(float(CandiateDictionary[candidate])/float(totalvotes),2)

        # we need to print the data in our text file for these results while in the loop and print them
        print(f"{candidate}: {percentage: .3%} ({CandiateDictionary[candidate]})")
        csvwriter.writerow([f"{candidate}: {percentage: .3%} ({CandiateDictionary[candidate]})"])

        #to find the winner. Create a variable to hold the largest number of votes
        votes = CandiateDictionary[candidate]


        #write a statement to compair the largest number of votes to the current candidate in the dictionary
        if votes > votespercandidate:
            votespercandidate = votes
            winner = candidate

    #print the last bit of data to our text doc and print
    print(f"Winner: {winner}")
    csvwriter.writerow([f"-------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow([f"-------------------"])






   


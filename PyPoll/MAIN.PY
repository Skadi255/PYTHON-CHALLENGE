#All my imports 
import os
import csv 
from statistics import mean


#Variable definitions 
vote_total = 0        #Holds the vote total 
candidate = []        #List that holds the candidate names
vote_percent = []     #List that holds percent vote per candidate
vote_val = []         #List that holds number of votes per candidate
check = "str"         #Compares first candidate value to arbituary val
winner = str          #Holds the winning candidate
check2 = -1           #Value to compare each candidates votes to 


#Opens the path PyPoll is diferent due to the online IDE
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csv_elec:

  csvreader = csv.reader(csv_elec, delimiter = ',')
  
  csv_header = next(csvreader)

  print(csv_header)

  #Main loop that reads in all the data 
  for row in csvreader:

    #Counts the total number of votes cast
    vote_total = vote_total + 1

    #Shows all the candidates that got votes

    #First checks for rows againt and arbituary value 
    if row[2] != check:
      
      #Checks if the value of row is alredy in candidate list
      if row[2] not in candidate:

        #If the candidate is unique it is added to the list
        candidate.append(row[2])

        #Initial a list that to hold votes for each candidate with matching indexs as candidate
        vote_val.append(0)
        vote_percent.append(0.0)
        
        #Resets the check value to check for other unique candidate names 
        check = row[2]

    #Calculates the total number of votes per candidate

    #Checks the candidate based on the list index then uses that index to update 
    #coreponding vote total. 
    if candidate[candidate.index(row[2])] == row[2]:
      vote_val[candidate.index(row[2])] = vote_val[candidate.index(row[2])] + 1
    
  #Calculate the percent for each candidate and calculate winner as well 
  for x in range(len(candidate)):
    vote_percent[x] = round((vote_val[x]/vote_total) * 100, 3)

    #Checks for highest vote in the candidate list
    if vote_val[x] > check2:
      winner =  candidate[x] 
      check2 = vote_val[x]

#Open the txt file in writinf mode
outpath = os.path.join('analysis', 'analysis.txt')

with open(outpath, 'w') as txtfile:

  txtfile.write('\n')
  txtfile.write("\nElection Results")
  txtfile.write("\n-------------------------------------")
  txtfile.write(f"Total Votes: {vote_total}")
  txtfile.write("\n-------------------------------------")
  for i in range(len(candidate)):
    txtfile.write(f"\n{candidate[i]}: {vote_percent[i]}% ({vote_val[i]})")
  txtfile.write("\n-------------------------------------")
  txtfile.write(f"Winner: {winner}")
  txtfile.close()
  
      
  #Print all the display data 
  print()
  print("Election Results")
  print("-------------------------------------")
  print(vote_total)
  print("-------------------------------------")
  for i in range(len(candidate)):
    print(f"{candidate[i]}: {vote_percent[i]}% ({vote_val[i]})")
  print("-------------------------------------")
  print(f"Winner: {winner}")
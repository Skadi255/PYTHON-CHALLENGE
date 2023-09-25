import os      #Os for reading csv files
import csv     #CSV for reading csv files 
from statistics import mean #For calculating the mean 

month_num = 0           #Number of months 
profit_total = 0        #Total prfit value 
profit_up = -5000000000 #Very small number to compare for max
profit_dow = 5000000000 #Very large number to compare for min       #
new_val = 0             #Used to hold a vale to calculate diffence between months 
profit_delta = []       #Change in profit values
month_val = []          #Holds the change months 
high_month = str        #Holds the High Month
low_month = str         #Holds the low Month
avg_change = float      #Holds avg change through months 

#Opens the file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#Opens the csv file 
with open(csvpath) as csvfile: 

    #Reads in the csv file
    csvreader = csv.reader(csvfile, delimiter = ',') 

    #Ignores the heading
    csv_header = next(csvreader)  

    #Main loop that goes through each values in the csv file
    for row in csvreader:   
        
        #Counts the number of months 
        month_num = month_num + 1

        #Totals the Profit/Losses
        profit_total = profit_total + int(row[1])

        #Calculates the changes per month, first value is not relivant will be removed 
        month_val.append(row[0])
        profit_delta.append(int(row[1]) - new_val)
        new_val = int(row[1])

    #Deletes the first value in the list 
    profit_delta.pop(0)
    month_val.pop(0)

    #Loops throught list profit delta   
    for i in range(len(profit_delta)):
        
        #Checks for max
        if (profit_up < profit_delta[i]):
            profit_up = profit_delta[i] 

        #Checks for min
        if (profit_dow > profit_delta[i]):
            profit_dow = profit_delta[i] 

#Shows the month with highes change
high_month = month_val[profit_delta.index(profit_up)]

#Shows the month with negative change
low_month = month_val[profit_delta.index(profit_dow)]

#Holds the average change
avg_change = mean(profit_delta)

#Opens the txt file in writing mode
out_path = os.path.join('analysis','analysis.txt')

with open(out_path, 'w') as txtfile:

    #Prints all the values to txt file
    txtfile.write('Financial Analysis')
    txtfile.write('\n----------------------')
    txtfile.write(f"\nTotal Months: {month_num}")
    txtfile.write(f"\nTotal: ${profit_total}")
    txtfile.write(f"\nAverage Change: ${avg_change}")
    txtfile.write(f"\nGreatest Increase in Profits: {high_month} (${profit_up})")
    txtfile.write(f"\nGreatest Decrease in Profits: {low_month} (${profit_dow})")
    txtfile.close() 

#Dispays values on the terminal 
print("Financial Analysis")
print("------------------")
print(f"Total Months: {month_num}")
print(f"Total: ${profit_total}")
print(f"Average Chage: ${avg_change}")
print(f"Greatest Increase in Profits: {high_month} (${profit_up})")
print(f"Greatest Decrease in Profits: {low_month} (${profit_dow})")

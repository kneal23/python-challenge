#First import packages to be used
import os
import csv

budget_data = os.path.join('/Users/keshia/Desktop/Bootcamp Challenges/python-challenge/PyBank','Resources',
                           'budget_data.csv')
with open (budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter="_")
    for row in csvreader:
        print(row)

#The total number of months included in the dataset
#create  variable (month) and use a for loop as it reads each row and make sure to add 'i+1'; total row +1
month = []

with open (budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    for row in csv_reader:      
        month.append(row[0]) 
    then: len(month)

print(f"Total Months:",len(month))


#The net total amount of "Profit/Losses" over the entire period
import csv

# Define the path to your CSV file
budget_data = '/Users/keshia/Desktop/Bootcamp Challenges/python-challenge/PyBank/Resources/budget_data.csv'

profit = []

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip the header row
    for row in csv_reader:      
        profit.append(int(row[1])) 

# Calculate the net total amount of profit/losses
net_total = sum(profit)

# Print the net total amount of profit/losses
print("Total:", net_total)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
# Define the path to your CSV file
budget_data = '/Users/keshia/Desktop/Bootcamp Challenges/python-challenge/PyBank/Resources/budget_data.csv'

# Initialize a list to store profit/loss values
profits = []

# Read the CSV file and extract profit/loss values
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip the header row
    for row in csv_reader:      
        profits.append(int(row[1])) 

# Calculate the changes in profit over the entire period
profit_changes = [profits[i+1] - profits[i] for i in range(len(profits)-1)]

# Calculate the average of the changes in profit
average_change = sum(profit_changes) / len(profit_changes)
rounded_number = round(average_change)

# Print the change in profit over the entire period and the average change
print("Change in profit over the entire period:", sum(profit_changes))
print("Average change in profit:", rounded_number)



#The greatest increase in profits (date and amount) over the entire period

# Define the path to your CSV file
budget_data = '/Users/keshia/Desktop/Bootcamp Challenges/python-challenge/PyBank/Resources/budget_data.csv'

# Initialize variables to store the greatest increase and its corresponding date
max_increase = 0
max_increase_date = ""

# Read the CSV file and extract profit/loss values and dates
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip the header row
    previous_profit = None
    for row in csv_reader:
        current_date = row[0]
        current_profit = int(row[1])
        
        # Skip the first row since there's no previous profit to compare with
        if previous_profit is not None:
            # Calculate the profit increase compared to the previous month
            profit_increase = current_profit - previous_profit
            
            # Check if the current increase is greater than the maximum increase found so far
            if profit_increase > max_increase:
                max_increase = profit_increase
                max_increase_date = current_date
        
        # Update the previous profit for the next iteration
        previous_profit = current_profit

# Print the greatest increase in profits (date and amount) over the entire period
print("The greatest increase in profits:")
print("Date:", max_increase_date)
print("Amount:", max_increase)




#The greatest decrease in profits (date and amount) over the entire period
# Define the path to your CSV file
budget_data = '/Users/keshia/Desktop/Bootcamp Challenges/python-challenge/PyBank/Resources/budget_data.csv'

# Initialize variables to store the greatest decrease and its corresponding date
max_decrease = 0
max_decrease_date = ""

# Read the CSV file and extract profit/loss values and dates
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Skip the header row
    previous_profit = None
    for row in csv_reader:
        current_date = row[0]
        current_profit = int(row[1])
        
        # Skip the first row since there's no previous profit to compare with
        if previous_profit is not None:
            # Calculate the profit decrease compared to the previous month
            profit_decrease = previous_profit - current_profit
            
            # Check if the current decrease is greater than the maximum decrease found so far
            if profit_decrease > max_decrease:
                max_decrease = profit_decrease
                max_decrease_date = current_date
        
        # Update the previous profit for the next iteration
        previous_profit = current_profit

# Print the greatest decrease in profits (date and amount) over the entire period
print("The greatest decrease in profits:")
print("Date:", max_decrease_date)
print("Amount:", max_decrease)


#Write to new CSV file and output language
output_file = 'PyBank_analysis.csv'
# Write to the new CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Total Months", "Total", "Change in profit over the entire period", "Average change in profit", "The greatest increase in profits",
                    "Data", "Amount", "The greatest decrease in profits", "Date", "Amount"])




# Add a txt file and pen a text file in write mode
with open('output.txt', 'w') as f:
    print(f"Total Months: {len(month)}", file=f)
    print(f"Total: {net_total}", file=f)
    print(f"Change in profit over the entire period: {sum(profit_changes)}", file=f)
    print(f"Average change in profit: {rounded_number}", file=f)
    print("The greatest increase in profits:", file=f)
    print(f"Date: {max_increase_date}", file=f)
    print(f"Amount: {max_increase}", file=f)
    print("The greatest decrease in profits:", file=f)
    print(f"Date: {max_decrease_date}", file=f)
    print(f"Amount: {max_decrease}", file=f)


#We did it! Help from ChatGPT and getting the flow of things. 
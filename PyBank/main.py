import pandas as pd
import os
import csv

# import the CSV file
#budgetdata = pd.read_csv('/Users/soniamoretti/Documents/TDM-VIRT-DATA-PT-06-2024-U-LOLC-main/03-Python/Starter_Code/PyBank/Resources/budget_data.csv')
#print(data.head())

# Set path for file
#csvpath = os.path.join("..", "Resources", "budget_data.csv")


# Initialize variables
total_months = 0
net_total = 0
monthly_changes = []
greatest_increase = 0
greatest_decrease = 0
previous_profit_loss = 0

# Read the CSV file
with open('/Users/soniamoretti/Documents/TDM-VIRT-DATA-PT-06-2024-U-LOLC-main/03-Python/Starter_Code/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    b_data = csv.reader(csvfile)
    next(b_data)  # Skip the header row
    
    for row in b_data:
        # Calculate total months and net total
        total_months += 1
        net_total += int(row[1])
        
        # Calculate monthly changes
        if previous_profit_loss != 0:
            change = int(row[1]) - previous_profit_loss
            monthly_changes.append(change)
            
            # Update greatest increase and decrease
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        previous_profit_loss = int(row[1])

# Calculate average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Print the results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the analysis results to a text file
with open("analysis_results.txt", "w") as file:
    file.write("Financial Analysis" + "\n")
    file.write("-------------------------" + "\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total: $" + str(net_total) + "\n")
    file.write("Average Change: $" + str(average_change) + "\n")
    file.write("Greatest Increase: " + str(greatest_increase_date) + " $" + str(greatest_increase) + "\n")
    file.write("Greatest Decrease: " + str(greatest_decrease_date) + " $" + str(greatest_decrease) + "\n")

print("Analysis results exported to analysis_results.txt")



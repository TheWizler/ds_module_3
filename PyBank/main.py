#Total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

import csv
import os

# Path to the dataset
file_path = 'PyBank/Resources/budget_data.csv'

# Create the Analysis folder if it doesn't exist
output_folder = 'PyBank/Analysis'
os.makedirs(output_folder, exist_ok=True)

# Initialize variables
total_months = 0
total_profit_loss = 0
prev_profit_loss = None
changes = []
greatest_increase = ["", 0]  # Greatest Decrease
greatest_decrease = ["", 0]  # Greatest Increase

# Open CSV
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    # Iterate over each row
    for row in reader:
        date, profit_loss = row
        profit_loss = int(profit_loss)

        # months
        total_months += 1

        # "Profit/Losses"
        total_profit_loss += profit_loss

        # change in "Profit/Losses"
        if prev_profit_loss is not None:
            change = profit_loss - prev_profit_loss
            changes.append(change)

            # Check for greatest increase and decrease in profits
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        # Update previous profit/loss
        prev_profit_loss = profit_loss

# Calculate the average change in "Profit/Losses"
average_change = sum(changes) / len(changes) if changes else 0

# Prepare output
output = (
    "Analysis\n"
    "--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Define the output file path within the Analysis folder
output_file_path = os.path.join(output_folder, 'analysis_output.txt')

# Print to terminal
print(output)

# Write results to the text file in the Analysis folder
with open(output_file_path, 'w') as output_file:
    output_file.write(output)

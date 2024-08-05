import os
import csv

budget_data = "PyBank/Resources/budget_data.csv"
total_months = 0  # Initialize total_months

# Initialize lists for storing data
dates = []
profits = []

# Total profit/loss variables
total_pl = 0

# Opening and reading the CSV file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Reading the header row
    csv_header = next(csvreader)

    # Reading the first row (so that we track the changes properly)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    # Going through each row of data after the header & first row
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])

        # Calculate the change, then add it to the list of changes
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

        # Total number of months
        total_months += 1

        # Total net amount of "Profit/Losses over the entire period"
        total_pl = total_pl + int(row[1])

    # Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Greatest decrease (lowest increase) in profits
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Average change in "Profit/Losses between months over the entire period"
    avg_change = sum(profits) / len(profits)

# Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_pl}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})")

# Exporting to .txt file
output = open("output.txt", "w")

# Exporting to .txt file
with open("output.txt", "w") as output:
    output.write(f"Financial Analysis\n")
    output.write(f"---------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total: ${total_pl}\n")
    output.write(f"Average Change: ${round(avg_change, 2)}\n")
    output.write(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})\n")
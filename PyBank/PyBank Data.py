import os
import csv

budget_data_csv = os.path.join("PyBank/Resources/budget_data.csv")

total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
months = []


with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    csv_header = next(csvreader)

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        profit_change = int(row[1]) - previous_profit
        previous_profit = int(row[1])
        profit_changes.append(profit_change)
        months.append(row[0])


average_change = sum(profit_changes[1:])/len(profit_changes[1:])

maximum_increase = max(profit_changes)
maximum_decrease = min(profit_changes)
maximum_increase_month = months[profit_changes.index(maximum_increase)]
maximum_decrease_month = months[profit_changes.index(maximum_decrease)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:{total_months}")
print(f"Total: ${net_total}")
print(f"Average: ${average_change:.2f}")
print(f"Greatest Increase: {maximum_increase_month} (${maximum_increase})")
print(f"Greatest Decrease: {maximum_decrease_month} (${maximum_decrease})")

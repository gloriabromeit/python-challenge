file = "../Documents/GitHub/python-challenge/PyBank/budget_data.csv"

import csv

with open(file) as revenue_data:
    reader = csv.reader(revenue_data)

    next(reader) 
    revenue = []
    date = []
    rev_change = []

    for row in reader:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total: $", sum(revenue))

    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])


    print("Average Change: $", round(avg_rev_change))
    print("Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")
 
    
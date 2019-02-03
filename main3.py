import os
import csv

my_file = os.path.join('', 'budget_data.csv')

"""Create lists for seperately storing all months, profit/loss figures, calculated differences in P/L, 
and a master list of lists to store all data with P/L converted to float type"""

month_list = []
P_L_List = []
P_L_Difference = []
master_list = []

"""Open csv file and create reader object so we can pull data into lists. Iterate through reader to append month data, P/L data, 
and a master set of data into respective lists. Convert P/L data to float type where necessary."""

with open (my_file, "r", newline="") as CsvFile:
    csv_reader = csv.reader(CsvFile)
    next(csv_reader)
    for row in csv_reader:
        month_list.append(row[0])
        P_L_List.append(float(row[1]))
        master_list.append([row[0], float(row[1])])

#Calculate toal months by finding size of the months list we created

month_count = len(month_list)

#Calculate total P/L by adding up all elements of P/L list.

P_L_Sum = sum(P_L_List)

"""Iterate through P/L list using indexes. The differences are calculated by subtracting the 
current list element from the next list element. Append these values to our list for storing differences. 
Find avg difference by adding all elements of differences list and dividing by the size of the list."""

for i in range(len(P_L_List) -1):
    P_L_Difference.append(P_L_List[i+1] - P_L_List[i])
P_L_Avg_Diff = sum(P_L_Difference)/len(P_L_Difference)

"""Create tracker variables for greatest increase and month of greatest increase. 
Iterate through master list and take difference between next P/L figure and current P/L figure. 
If this value is greater than the value currently stored in our greatest increase tracker, 
set current P/L value to greatest and pull the month of the next element, since P/L changes will be measured in the second month.""" 

greatest_increase = 0
greatest_inc_month = ""
for i in range(len(master_list)-1):
    if ( master_list[i+1][1] - master_list[i][1] ) > greatest_increase:
        greatest_increase = master_list[i+1][1] - master_list[i][1]
        greatest_inc_month = master_list[i+1][0]

"""Follow process similar to above calculation of greatest increase to get greatest decrease. 
Instead of checking if P/L difference is greater than the current value of our gratest decrease tracker, 
we want to check if it is less than this value""" 

greatest_decrease = 0
greatest_dec_month = ""
for i in range(len(master_list)-1):
    if ( master_list[i+1][1] - master_list[i][1] ) < greatest_decrease:
        greatest_decrease = master_list[i+1][1] - master_list[i][1]
        greatest_dec_month = master_list[i+1][0]

#Print formatted text showing desired output figures

print(f"""\
    Financial Analysis
    -------------------------
    Total Months: {month_count}
    Total: {P_L_Sum}
    Average Change: {P_L_Avg_Diff}
    Greatest Increase in Profits: {greatest_inc_month} ({greatest_increase})
    Greatest Decrease in Profits: {greatest_dec_month} ({greatest_decrease})
    """)

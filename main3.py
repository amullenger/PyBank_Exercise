import os
import csv

my_file = os.path.join('', 'budget_data.csv')

month_list = []
P_L_List = []
P_L_Difference = []
master_list = []


with open (my_file, "r", newline="") as CsvFile:
    csv_reader = csv.reader(CsvFile)
    next(csv_reader)
    for row in csv_reader:
        month_list.append(row[0])
        P_L_List.append(float(row[1]))
        master_list.append([row[0], float(row[1])])

month_count = len(month_list)

P_L_Sum = sum(P_L_List)

for i in range(len(P_L_List) -1):
    P_L_Difference.append(P_L_List[i+1] - P_L_List[i])
P_L_Avg_Diff = sum(P_L_Difference)/len(P_L_Difference)

greatest_increase = 0
greatest_inc_month = ""
for i in range(len(master_list)-1):
    if ( master_list[i+1][1] - master_list[i][1] ) > greatest_increase:
        greatest_increase = master_list[i+1][1] - master_list[i][1]
        greatest_inc_month = master_list[i+1][0]

greatest_decrease = 0
greatest_dec_month = ""
for i in range(len(master_list)-1):
    if ( master_list[i+1][1] - master_list[i][1] ) < greatest_decrease:
        greatest_decrease = master_list[i+1][1] - master_list[i][1]
        greatest_dec_month = master_list[i+1][0]

print(f"""\
    Financial Analysis
    -------------------------
    Total Months: {month_count}
    Total: {P_L_Sum}
    Average Change: {P_L_Avg_Diff}
    Greatest Increase in Profits: {greatest_inc_month} ({greatest_increase})
    Greatest Decrease in Profits: {greatest_dec_month} ({greatest_decrease})
    """)

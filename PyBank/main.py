#import libraries
import os
import csv
#join path
inpath = os.path.join("..", "PyBank","Resources", "budget_data.csv")
inpath 
#test the inpath
with open(inpath,  mode='r', encoding='ISO 8859-1') as csvfile:
    bankreader= csv.reader(csvfile, delimiter=',')

    bankheader= next(bankreader)
    linecount = 0
    profit_increment = 0
    month_list = []
    gross = []
    up_list=[]
    for line in bankreader:
        linecount = linecount + 1
        #changing line[1] to float
        line[1] = float(line[1])        
        ##print(line)
        gross.append(float(line[1]))
        month_list.append(line[0])
        sum(gross)
        #the number of data in gross started at 0 but line count started with 1 per loop/
        #so gross + 1 = linecount => gross = linecount - 1// and we want gross[1] - gross[0] ==> gross[linecount -1 -1= linecount-2]
        profit_increment = gross[linecount - 1] - gross[linecount - 2]
        up_list.append(profit_increment)
        
#line[1] is the second column
        #print(line[1])
    
print("Finanical Analysis")
print("--------------------------")
#Total Months
print(f"Total Months: {linecount}")
# total profit 
print(f"Total: ${sum(gross)}")
#Average Change
print(f"Average Change: ${(line[1]-gross[0])/(linecount-1)}")
#greatest increase #greatest decrease
max_up = up_list.index(max(up_list))
min_up = up_list.index(min(up_list))
print(f'Greatest Increase in Profits: {month_list[max_up]} ${max(up_list)}')
print(f'Greatest Decrease in Profits: {month_list[max_up]} ${min(up_list)}')
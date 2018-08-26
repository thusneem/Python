mport os
import csv
import datetime




    
budgetdata=os.path.join("budget_data.csv")
with open(budgetdata,'r') as csvfile:
    # csvreader - Python's obj; contains lines of csv file
    # row - list of strings returned
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)
    totalmonth = 0
    netpl=0
    pl_list=[]
    row_list=[]
    diff_row = []
     for row in csvreader:
        totalmonth += 1
        netpl += int(row[1])
        
        pl_list.append(row[1])
        row_list.append(row[0])
        
    
    for i in range(1,len(pl_list),1):
        # print(f"i is : {str(i)}")
        diff = 0
        diff =  int(pl_list[i]) - int(pl_list[i-1])
        diff_row.append(diff)

# finding average
avg = round(sum(diff_row)/len(diff_row),2)


# finding increase and decrease in profits
row_list.pop(0)
dates_dict = dict(zip(row_list,diff_row))
greatest_increase = [(values,keys)for keys,values in dates_dict.items()]
greatest_decrease = [(values,keys)for keys,values in dates_dict.items()]
# printing 
print(f"Total Months : {str(totalmonth)}")
print(f"Total : {str(netpl)}")
print(f"Average : {str(avg)}")
print(f"Greatest increase in  profits : {str(max(greatest_increase))}")
print(f"Greatest decrease in  profits : {str(min(greatest_decrease))}")




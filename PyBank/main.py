# module for reading data from a csv file
import csv
# operating systems module for creating and finding file
import os
# stores path to data file
path = os.path.join('Resources','budget_data.csv')
# opens data file in read mode and creates a var to call
with open ('budget_data.csv', 'r') as csv_file:
# calls csv module to read csv file
    csv_reader = csv.reader(csv_file)
# skips the header line
    next(csv_reader)
# creates a list to store monthly revenues
    revenue = []
    # creates a list to store each date
    date = []
    # creates a list to store each monthly change
    rev_change = []
    # loops through each row
    for row in csv_reader:
        # first value before comma will be stored in date
        date.append(row[0])
        #  second value will be stored under revenues
        revenue.append(float(row[1]))
    #now each date/month stored in a list, number of elements in that list will return total duration of records
    total_months=len(date)
    # looping through revenues to calculate monthly difference beginning from second element until the last one
    for i in range(1,len(revenue)):
        # adding each difference as a new list element
        rev_change.append(revenue[i] - revenue[i-1])
    # method below sums all list elements then operation divides returned value by the number of elements in the list to calculate average
    average_change = sum(rev_change)/len(rev_change)
    # method will return the best financial gain
    max_rev_change = max(rev_change)
    # index method will return the date with above while
        # last operation will shift date due to loop initialization above begins with 1 when compared to date array with 0 zero
    max_rev_change_date = str(date[rev_change.index(max(rev_change)) + 1])
    # method will return the worst financial loss on records in file
    min_rev_change = min(rev_change)
    # as explained above in max
    min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])
    # results printed in accounting format
    print("\n  < Financials of PyBank for ", date[0], " to ", date[total_months - 1],">")
    print("-------------------------------------------------------")
    print("Total Months:\t", len(date))
    print("Total: \t", '$ {:,.0f}'.format(sum(revenue)))
    print("Avereage Revenue Change: \t", '$ {:,.0f}'.format(average_change))
    print("Greatest Increase in Revenue: \t", max_rev_change_date, '$ {:,.0f}'.format(max_rev_change))
    print("Greatest Decrease in Revenue: \t", min_rev_change_date,'$ {:,.0f}'.format(min_rev_change))
# firstly creates a text document in the same folder by the help of imported os module
PyBank_output=os.path.join('PyBank_output.txt')
# opens the above text document in write mode of csv module
    #separated by tabs thus could be copy/pasted on a spreadsheet as rows and columns
with open(PyBank_output,'w') as txt_only:
    txt_only.writelines('-----ELECTION RESULTS-----\n')
    txt_only.writelines("  < Financials of PyBank for ")
    txt_only.writelines(date[0])
    txt_only.writelines(" to ")
    txt_only.writelines(date[total_months - 1])
    txt_only.writelines(">\n")
    txt_only.writelines("----------------------------------------------------")
    txt_only.writelines("\nTotal Months: \t")
    txt_only.writelines(str(len(date)))
    txt_only.writelines("\nTotal Revenues: \t")
    txt_only.writelines('$ {:,.0f}'.format(sum(revenue)))
    txt_only.writelines("\nAvereage Revenue Change: \t")
    txt_only.writelines('$ {:,.0f}'.format(average_change))
    txt_only.writelines("\nGreatest Increase in Revenue:\t")
    txt_only.writelines('$ {:,.0f}'.format(max_rev_change))
    txt_only.writelines("\t")
    txt_only.writelines(max_rev_change_date)
    txt_only.writelines("\nGreatest Decrease in Revenue:\t")
    txt_only.writelines('$ {:,.0f}'.format(min_rev_change))
    txt_only.writelines("\t")
    txt_only.writelines(min_rev_change_date)
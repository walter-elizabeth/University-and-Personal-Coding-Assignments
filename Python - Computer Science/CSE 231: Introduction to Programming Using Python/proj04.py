###############################################################################
# CSE 231
# Computer Project #4
#
# Algorithm
#   Import modules
#   Call function
#       Call function to find file
#           prompt for a year
#           try - except construct; prompt until file successfully opens
#           return file pointer
#       Call function to open file
#           read lines in data file, transform/organize data
#           return data in list
#       Call function to find average income 
#           Take in data list, sum list slice of values corresponding to total 
#              income of each interval
#	    Find last value in list slice corresponding to cumulative workers
#	      & divide sum of total income list by value, return calculation
#       Call function to find median income
#	    Take in data list, find index of interval where percent of total is 
#         closest to 50
#	        Return float value of average income in the interval at that index
#	    Display year, average income, and median income
#	    Prompt for string input. if input successful, call plotting function
#		    Display plot
#       Prompt user for input. loop while input is a valid
#	        Prompt for a percent (float value)
#		    if input valid, call function to find income threshold
# 	    	    in cumulative percentages list, find index where value == input 
#		        Display percent and corresponding interval min at index
#           else display error message
#	        Prompt for an income (float value)
#		    if valid call function to find list index of the relevant income 
#             interval and corresponding cumulative percentage at index
#		        Display income and corresponding percentage
#           else display error message
#           if no input, exit while loop
#       Else display error message and reprompt
###############################################################################

import pylab

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
def open_file():
    '''Prompt for a year and check if input can be converted to int.
       Check if int is within given range, if so search for file.
       If cannot be converted to int or file cannot be opened, 
       display error message and reprompt user until successfully opens file.
       Return file pointer and year
       '''
    year_str = input("Enter a year where 1990 <= year <= 2015: ")
    while True:
        try:
            year = int(year_str)
            if 1990 <= year <= 2015:
                file_name = 'year' + year_str + '.txt'
                try:
                    file = open(file_name, 'r')
                    return file, year
                    break
                except FileNotFoundError:
                    print('Error in file name:', file_name,' Please try again.')
                    year_str = input("Enter a year where 1990 <= year <= 2015: ")
            else:
                print('Error in year. Please try again.')
                year_str = input("Enter a year where 1990 <= year <= 2015: ")
        except ValueError:
            print('Error in year. Please try again.')
            year_str = input("Enter a year where 1990 <= year <= 2015: ")
   
        
def read_file(fp):
    '''Takes in a file pointer and returns a list of data in file'''
    rows_list = []
    low_end_range = [] # column 0
    high_end_range = [] # column 2
    num_ppl = [] # column 3
    cumulative_ppl = [] # column 4
    cumulative_percent = [] # column 5
    range_total_income = [] # column 6
    range_avg_income = [] # column 7  
    for line in fp:
        line = line.strip()
        new_list = []
        for char in line:
            line = line.replace(',', '') # remove commas
        line_list = line.split()
        for i in line_list:
            try:
                i = float(i)
                new_list.append(i)
            except ValueError:
                continue
        rows_list.append(new_list)
    rows_list = rows_list[2:]
    last_row = rows_list[-1]
    # solve for what "and over" is as a dollar amt // 
    # aka solve for max income in highest income interval using values from row
    x = ((last_row[5])*(last_row[1]))/(last_row[0]) 
    rows_list[-1].insert(1,x)
    for lst in rows_list:
        low_end_range.append(lst[0]) 
        high_end_range.append(lst[1])
        num_ppl.append(lst[2])
        cumulative_ppl.append(lst[3])
        cumulative_percent.append(lst[4])
        range_total_income.append(lst[5])
        range_avg_income.append(lst[6])
    list_by_cat = [low_end_range, high_end_range, num_ppl, cumulative_ppl,
                   cumulative_percent, range_total_income, range_avg_income]
    return list_by_cat
        
def find_average(data_lst):
    '''Takes a list of data and returns average salary'''
    avg_salary = sum(data_lst[5])/(data_lst[3][-1])
    return avg_salary
    
def find_median(data_lst):
    '''Takes a list of data and returns approximate median income'''
    cumulative_percent = data_lst[4]
    diff = 50
    a = 0
    b= 0
    for i in cumulative_percent:
        av = abs(50 - i)
        if av < diff:
            diff = av
            a = 50 - diff
            b = 50 + diff
    if a in cumulative_percent:
        med_index1 = cumulative_percent.index(a) # the i where diff is closest to 0 
    if b in cumulative_percent:
        med_index1 = cumulative_percent.index(b) # i where diff smallest, other side of 50
    med_income = data_lst[6][med_index1]
    return med_income
        
def get_range(data_lst,percent):
    '''Takes a list of data and a percent as a float and returns salary range
       as a tuple'''
    for i in data_lst[4]:
        if i >= percent:
            percent_val = i
            index1 = data_lst[4].index(i)
            lower_bound = data_lst[0][index1]
            upper_bound = data_lst[1][index1]
            avg_income = data_lst[6][index1]
            sal_range = lower_bound,upper_bound
            return sal_range, percent_val, avg_income
            break

def get_percent(data_lst,salary):
    '''Takes a list of data and an income as a float and returns income 
       interval it is in and the cumulative percentage that corresponds to the
       interval'''
    count = 0
    lower = data_lst[0]
    upper = data_lst[1]
    for i in lower: # for value in low_end list
        if i < salary: # if value is less than salary
            count += 1
    if lower[count] <= salary:
        if salary <= upper[count]:
            interval = lower[count], upper[count]
            c_percent = data_lst[4][count]
            return interval,c_percent
    
def main():
    data_file, year = open_file()
    data = read_file(data_file)
    avg = find_average(data)
    median = find_median(data)
    print('{:<6s}{:<14s}{:<14s}'.format('Year','Mean','Median'))
    print('{:<6d}${:<14,.2f}${:<14,.2f}'.format(year,avg,median))
    
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        xvals = data[0][:40] # income (lower bound of interval)
        yvals = data[4][:40] # cumulative percentage,
        my_plot = do_plot(xvals,yvals,year)
        print(my_plot)
        
    choice = input("Enter a choice: r for range, p for percent, or n to stop: ")
    while choice != "n":
        if choice == 'r':
            percent = float(input('Enter a percent: '))
            if percent in range(100):
                interval, p_val, avg_inc = get_range(data,percent)
                print("{:4.2f}% of incomes are below ${:<13,.2f}.".
                      format(percent,interval[0]))
            else:
                print("Error in percent. Please try again")
        elif choice == 'p':
            income = float(input('Enter an income: '))
            if income > 0:
                interval, c_percent = get_percent(data,income)
                print("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes."
                      .format(income,c_percent))
            else:
                print("Error: income must be positive")
        else:    
            print('Error in selection.')
        choice = input("Enter a choice: r for range, p for percent, or n to stop: ")

if __name__ == "__main__":
    main()
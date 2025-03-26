############################################################################
# Computer Project #3
#
# Algorithm
#   Call function
#       Call function to open file
#           prompt for a file name
#           try - except construct
#       Loop through lines in file
#           Call function to find min value (percentage) and index in line
#                Return float value and integer value
#           Call function to find max value (percentage) and index in line
#                Return float value and integer value
#           Call function to find value (year) in line at index
#                Return integer value
#           Call function to find value (year) in line at index
#                Return integer value
#           Call function to find min value in line at index
#                Return float value
#           Call function to find max value in line at index
#       Call function to display values with string formatting
#           Output min percentage, min year, min value, \
#           max percentage, max year, max value
############################################################################

# find min and max chg in GDP for yrs 1969 - 2015
# find GDP value for yr 1969 and yr 2015
# build following functions in order

def open_file():
    '''Repeatedly prompt until a valid file name allows the file to be opened.'''
    # takes no args, returns a file pointer
        # repeatedly prompt for file name until file successfully opens
    # use try- except construct, checking for FileNotFoundError exception
    input_boolean = False
    while not input_boolean:
        try:
            file = input("Enter a file name: ")
            fp = open(file, 'r')
            return fp
            input_boolean = True  
        except FileNotFoundError:
            print("Error. Please try again")

def find_min_percent(line):
    '''Find the min percent change in the line; return the value and the index.'''
    # takes in a line (string) from file and returns min value in that line and index showing wher min value is in the line
    # min_value is float, min_value_index is int
    # use range, slice string so that value of min_change_index is between 0 and 46
        # each year/data value becomes an index instead of each character in the string being an index
        # convert index to int
    index = 0
    min_value = 10**6
    for i in range(47):
        value = float(line[(76 + (i*12)):(76+(i*12)+12)])        
        index = i
        if value < min_value:
            min_value = value
            min_change_index = int(index)
    return min_value, min_change_index


def find_max_percent(line):
    '''Find the max percent change in the line; return the value and the index.'''
    # returns data value (float) and index (int)
    # same as find_min_percent() basically just flipped in loop comparing values
    index = 0
    max_value = -10**6
    for i in range(47):
        value = float(line[(76 + (i*12)):(76+(i*12)+12)])        
        index = i
        if value > max_value:
            max_value = value
            max_change_index = int(index)
    return max_value, max_change_index

def find_gdp(line, index):
    '''Use the index fo find the gdp value in the line; return the value'''
    # line looking at is line 44 and index corresponds to indexes returned from above 2 functions
        # one from find_min function when solving for min and one from find_max fuct when solving for max
    line = line.strip()
    gdp_value = float(line[(76 + (index*12)):(76+(index*12)+12)])
    return gdp_value

def find_year(line,index):
    '''Use index found above to find year in line; return the value '''
    year = int(line[(76 + (index*12)):(76+(index*12)+12)])
    return year
    
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    '''Display values; convert billions to trillions first.'''    
    min_val_gdp = min_val_gdp/1000 # convert to trillions 
    max_val_gdp = max_val_gdp/1000
    print('\nGross Domestic Product')
    print('{:<10s}{:>8s}{:>6s}{:>18s}'.format('min/max','change','year','GDP (trillions)'))
    print('{:<10s}{:>8.1f}{:>6d}{:>18.2f}'.format('min', min_val, min_year, min_val_gdp))
    print('{:<10s}{:>8.1f}{:>6d}{:>18.2f}'.format('max', max_val, max_year, max_val_gdp))
    
def main():                    
    fp = open_file()
    count = 0
    min_gdp_change = 0
    min_change_index = 0
    max_gdp_change = 0
    max_change_index = 0
    min_gdp_val = 0
    max_gdp_val = 0
    min_year = 0
    max_year = 0
    for line in fp:
        count +=1
        if count == 8:
            year_line = line
            year_line = year_line.strip()
        if count == 9:
            gdp_change_line = line
            gdp_change_line = gdp_change_line.strip()
            # call function
            min_gdp_change, min_change_index = find_min_percent(gdp_change_line) #line 9 is input
            max_gdp_change, max_change_index = find_max_percent(gdp_change_line)
            # call function
            min_year = find_year(year_line, min_change_index) # line 8 is 1st input
            max_year = find_year(year_line, max_change_index)
        if count == 44:
            gdp_value_line = line
            gdp_value_line = gdp_value_line.strip()
            # call function
            min_gdp_val = find_gdp(gdp_value_line, min_change_index) #1st input is line 44
            max_gdp_val = find_gdp(gdp_value_line, max_change_index)
    
    display(min_gdp_change, min_year, min_gdp_val, max_gdp_change, max_year, max_gdp_val)
    

# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()

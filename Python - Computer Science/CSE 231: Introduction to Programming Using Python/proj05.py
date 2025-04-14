###############################################################################
# CSE 231
# Computer Project #5
#
# Algorithm
#   call function to get file pointer
#     prompt for a file name (csv)
#     input a valid file name
#     return file pointer
#   call function to read file
#     loop through lines in file
#       index and modify lines
#   return dictionary
#   call function to find min and max tuple values
#   output dictionary keys in alpha order (crop), header, values for dictionary
#    in alpha order (state), tuple elements (year, val) corresponding to max 
#    and min for each value (state)
#
###############################################################################

import string
import csv
from operator import itemgetter

STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado',
          'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 
          'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
          'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 
          'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 
          'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
          'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 
          'West Virginia', 'Wisconsin', 'Wyoming']

def open_file():
    '''
    takes no args, prompts for file name
    displays error message if file name 
       not found and repropmpts
    returns file pointer
    '''
    input_boolean = False
    while not input_boolean:
        try:
            file = input("Enter a file: ")
            fp = open(file, 'r')
            return fp
            input_boolean = True  
        except IOError:
            print("Error. Please try again")

def read_file(fp):
    ''' 
    Reads in a csv file and returns a dictionary 
    fp: a file pointer
     initialize a dictionary
     index line in file to create new variables,
      clean state values (str) of extraneous characters
      exclude lines where value (str) is empty or not digits
         and convert remaining value values to float
      exclude lines where state values are not in STATES (list)
      exclude lines where variety values (str) are not 
        the given val (str)
      add crop (str) key, value (empty dict) pair to dictionary
        if key is not in dictionary
      add state (str) key, value (empty list) to nested 
        dictionary if key doesn't exist
      append tuple (year (int), value (int)) to value (list)
        in nested list if year value not in dictionary
    close input file
    returns a dictionary
    '''
    reader = csv.reader(fp)
    next(reader,None)
    data_dict = {} # will be list that is value for dict2 (crop in main key)
    for line in reader:
        state = line[0]
        crop = line[1]
        variety = line[3]
        year = int(line[4])
        value = line[6]
        for char in state:
            if char.isalpha() == False:
                state = state.replace(char,' ') #should take care of the missouri mispelling problem
            state = state.strip()
        if value != '':
            if value.isdigit() == True:
                value = int(value)  
                if state in STATES: # dont want rows for "other states", etc, only for rows w/state name that is in STATES list
                    if variety == 'All GE varieties': # only want this type of variety / only want rows where variety is 'All GE varieties'
                        if crop not in data_dict:
                            data_dict[crop] = {} # first dict w/crop keys and new dict for values
                        if state not in data_dict[crop]:
                            data_dict[crop][state] = []# state is a key to a nested dict w/ empty list for vals                
                        info = year,value
                        if year not in data_dict[crop][state]:
                                data_dict[crop][state].append(info)
                                
    fp.close() # input file must be closed inside function
    return data_dict

def find_vals(data_dict):
    ''' 
    Indexes, sorts, and iterates through dictionary using lists
    data_dict: main dictionary for contents of file
     Iterate through dictionary keys and values, sort keys and 
       values by creating lists
     Sort values (tuple) in nested dictionary to find tuple with
       largest value and tuple with smallest value for each key 
       (str) in nested dictionary
     Iterates through lists 
    outputs: main dict key in alphabetical order by crop name (str),
      header, corresponding value (dict) for each key in alphabetical
      order; elements (int) of tuples found in value (list)
      representing the smallest and largest values (int), 
      and corresponding years (int) in each state key, value
    '''
    #OUTPUT:
        # by crop, ordered alphabeticall by crop name (crop column) - crop = key
        # data output alpha by state name for ea crop - value = state name
            # {crop[list of states]}
            
    crop_list = sorted(data_dict.items(), key = itemgetter(0))
    for crops, crop_dict in crop_list:
        print('Crop:', crops)
        print('{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}'.format('State','Max Yr', 'Max', 'Min Yr', 'Min'))
        states_list = sorted(crop_dict.items(), key = itemgetter(0))
        for state, tup_list in states_list:
            min_sort = sorted(tup_list, key = itemgetter(1,0))
            min_tuple = min_sort[0]
            min_val = min_tuple[1]
            min_yr = min_tuple[0]
            max_sort = sorted(tup_list, key = itemgetter(1), reverse = True)
            max_tuple = max_sort[0]
            max_val = max_tuple[1]
            max_yr = max_tuple[0]
            print('{:<20s}{:<8d}{:<6d}{:<8d}{:<6d}'.format(state, max_yr, max_val, min_yr, min_val)) 
            # in the project intro video he changed all year values to int so I reformatted descriptor codes
              
def main():
    crop_file = open_file()
    dict1 = read_file(crop_file)
    find_vals(dict1)
    

if __name__ == "__main__":
    main()
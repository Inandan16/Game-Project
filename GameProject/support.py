from csv import reader
from settings import *


# function to read and import csv level data
def import_level_data(path):
    # array variable to hold the values of the csv file
    level_data = []

    # opens the csv file with level data
    with open(path) as map:
        # this will read the data from the csv file
        # the delimiter tells the program how to separate different values, in this case, it is a comma
        # the 'list' will turn the data type of the data to a list
        data = list(reader(map, delimiter=','))

        # for loops will store the list data into the array within a variable
        for row in data:
            level_data.append(row)
        return level_data


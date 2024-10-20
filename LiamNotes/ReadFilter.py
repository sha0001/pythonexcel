
#Reading a csv file into an array with a filter 

import csv 
import pprint

def read_csv_filter_rows(filename, filter_func):
    # filter_func is referencing our filter function below. 
    # creating array to hold the filtered data
    filtered_data = []

    with open(filename,'r') as csvfile: 
        reader = csv.reader(csvfile)
        for row in reader: 
            if (filter_func(row)):
                filtered_data.append(row) 
                # this for loop will only add a row to the array if the filter function returns true. 
    return filtered_data

# Filter Function 
def filter_by_category(row, category): 
    return row[1] == category 
# if the category column in a row contains the category we want, return 'True'/ 

# Call the read function with a filter function 
filtered_rows = read_csv_filter_rows("Inventory.csv", lambda row: filter_by_category(row, "Fruits" )) 

# Print filtered data
pprint.pprint(filtered_rows)


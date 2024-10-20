# Converts a csv file into a python array. 

import csv 

def read_to_array(filename): 
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader: 
            data.append(row)
    return data

inventory_data = read_to_array("Inventory.csv")
print(f"Items: {len(inventory_data)}") # Print the length of the array
print(inventory_data[0]) #Print the header data
print(inventory_data[1]) #Print the first row of data
print(inventory_data[1][0], inventory_data[1][2]) #print data at row 1 index zero, and row 1 index 2. 



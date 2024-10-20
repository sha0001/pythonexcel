
## Converts csv file into a python dictionary 

import csv 
import pprint

def read_csv_to_dict(filename): 
    data = {}
    with open(filename,'r') as csvfile: 
        reader=csv.DictReader(csvfile)
        for row in reader: 
            data[row[reader.fieldnames[0]]] = row

# reader.fieldnames gives us the header data for a dictionary 
# This would be the first row in our csv file. 

    return data

#Example usage 
inventory_data = read_csv_to_dict("Inventory.csv") 

#Accessing data 

pprint.pprint(inventory_data) 
pprint.pprint(inventory_data["Apple"]) 
pprint.pprint(inventory_data["Apple"] ["Consumer Price"])

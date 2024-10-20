
# Writing CSV file from an array 

import csv


# declare the sample data
data = [
  {"Item Name":"Apple", "Category":"Fruits", "Quantity":100, "Wholesale Price":0.50, "Consumer Price":0.75},
  {"Item Name":"Banana", "Category":"Fruits", "Quantity":150, "Wholesale Price":0.35, "Consumer Price":0.50},
  {"Item Name":"Orange", "Category":"Fruits", "Quantity":120, "Wholesale Price":0.45, "Consumer Price":0.65},
  {"Item Name":"Grapes", "Category":"Fruits", "Quantity":80, "Wholesale Price":0.60, "Consumer Price":0.85},
  {"Item Name":"Strawberries", "Category":"Fruits", "Quantity":90, "Wholesale Price":1.20, "Consumer Price":1.50}
]

# define the column names that will be the header row
# This is required by the dictwriter object in the csv module
# so it knows how to match each dictionary key to each column 

fieldnames=["Item Name","Category","Quantity","Wholesale Price","Consumer Price"]

# function to write the data
def write_dict_to_csv(data,filename):
    with open(filename,'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# write the data to the file

write_dict_to_csv(data,"output.csv") 

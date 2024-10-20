## Add a column to the inventory.csv file programatically

# There are currently two prices for columns: Wholesale and Consumer price. 

# The challenge is to add a third price column "margin" that shows the difference between the two. 

# Output this as a new file "margin.csv" 


import csv 

# defining functions 

## read csv to array
def read_to_array(filename):
    data = []
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader: 
            data.append(row) 
        return data

## write array to csv 
def write_array_to_csv(data,filename):
    with open(filename,'w',newline='') as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerows(data) 

#read the csv file to an array 
inventory_data = read_to_array("Inventory.csv") 

#Create new header 'margin' 

inventory_data[0].append('Margin')

#calculate the new column and append the new column

# The 4th and 5th columns are listed as strings in the array, so these are converted to float, 
#then the "{:.2f}.format() function rounds the floats to a decimal representation. 
# Keep in mind that this is often not accurate, but it seems to work in this example. 
# 
for n in inventory_data[1:]:
    margin = "{:.2f}".format( float(n[4])-float(n[3]))
    n=n.append(margin)

#write to new file
write_array_to_csv(inventory_data,"append.csv")


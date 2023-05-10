#Joshua Perez
#ID:1837170
#importing modules for date time and csv 
import csv
from datetime import datetime
#creating functions to sort specific rows for upcoming files
def first_row_sort(row):
    return row[0]
def second_row_sort(row):
    return row [1]
def third_row_sort(row):
    return row [2]
def fourth_row_sort(row):
    return row [3]
#Creating multiple lists to pull csv data into
manfaclist =[]
price_list=[]
service_date=[]
damaged_column=[]
#creating lists to take device items
device_list =[]
laptop_list = []
tower_list = []
phone_list =[]
#creating list for damaged items
damaged_list = []
#past service dates list 
past_list = []
#opening files to pull data from and adding to different files
with open('ManufacturerList.csv', 'r') as file:
    reader = csv.reader(file)
    sorted_rows = sorted(reader, key=first_row_sort)
    for line in sorted_rows:  
        manfaclist.append(line[0:3])
        damaged_column.append(line[3])
        device_list.append(line[0:2])
with open('PriceList.csv', 'r') as file:
    reader = csv.reader(file)
    sorted_rows = sorted(reader, key=first_row_sort)
    for row in sorted_rows:
        price_list.append(row[1])
with open('ServiceDatesList.csv', 'r') as file:
    reader = csv.reader(file)
    sorted_rows = sorted(reader, key=first_row_sort)
    for i in sorted_rows:
        service_date.append(i[1])
#appending columns of data that are needed for different files
for x in range(0,len(manfaclist)):
    manfaclist[x].append(price_list[x])
for x in range(0,len(manfaclist)):
    manfaclist[x].append(service_date[x])
for x in range(0,len(manfaclist)):
    manfaclist[x].append(damaged_column[x])
for x in range (0,len(device_list)):
    device_list[x].append(price_list[x])
    device_list[x].append(service_date[x])
    device_list[x].append(damaged_column[x])
#beginning of file creation and sorting it by manufacturer type
with open('FullInventory.csv', 'w') as file:
    writer = csv.writer(file)
    sorted_rows = sorted(manfaclist, key=second_row_sort)
    writer.writerows(sorted_rows)


#Creating csv file for items that have status of damaged and in order of price
for laptop in range(0,len(manfaclist)):
    if manfaclist[laptop][2] == "laptop":
        laptop_list.append(device_list[laptop])
# sorting the csv data in price reverse so its highest to lowest
with open("LaptopInventory.csv","w",newline="") as lpi:
    lap_writer = csv.writer(lpi)
    sorted_rows = sorted(laptop_list, key=first_row_sort)
    lap_writer.writerows(laptop_list)

#Creating csv file for items that have status of damaged and in order of price
for phone in range(0,len(manfaclist)):
    if manfaclist[phone][2] == "phone":
        phone_list.append(device_list[phone])
# sorting the csv data in price reverse so its highest to lowest
with open("PhoneInventory.csv","w",newline="") as ppi:
    phone_writer = csv.writer(ppi)
    sorted_rows = sorted(phone_list, key=first_row_sort)
    phone_writer.writerows(phone_list)

#Creating csv file for items that have status of damaged and in order of price
for tower in range(0,len(manfaclist)):
    if manfaclist[tower][2] == "tower":
        tower_list.append(device_list[tower])
# sorting the csv data in price reverse so its highest to lowest
with open("TowerInventory.csv","w",newline="") as twi:
    phone_writer = csv.writer(twi)
    sorted_rows = sorted(phone_list, key=first_row_sort)
    phone_writer.writerows(tower_list)

#Creating csv file for items that have status of damaged and in order of price
for damaged in range(0,len(manfaclist)):
    if manfaclist[damaged][5] == "damaged":
        damaged_list.append(manfaclist[damaged][0:5])
# sorting the csv data in price reverse so its highest to lowest
with open("DamagedInventory.csv","w",newline="") as dml:
    dam_writer = csv.writer(dml)
    sorted_rows = sorted(damaged_list,key=third_row_sort,reverse=True)
    dam_writer.writerows(damaged_list)
# Creating final file dependent on if the service date has passed 
for past in range(0,len(manfaclist)):
    date_str = manfaclist[past][4]
    date_obj = datetime.strptime(date_str, '%m/%d/%y')
    if date_obj < datetime.now():
        past_list.append(manfaclist[0:6])
#sorting the file column by the service date
with open("PastServiceDatesInventory.csv","w", newline = "") as psd:
    past_writer = csv.writer(psd)
    sorted_rows = sorted(past_list, key=fourth_row_sort)
    past_writer.writerows(past_list)
    

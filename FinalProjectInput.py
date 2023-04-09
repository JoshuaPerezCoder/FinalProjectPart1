#Name:Joshua Perez StudentID:1837170
#importing mudules to sort and open csv files
import csv
import operator
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
#pulling data from the manufacturer csv file by sorting ID
with open("ManufacturerList.csv") as manlist:
    ml = csv.reader(manlist,delimiter=",")
    sort = sorted(ml,key= operator.itemgetter(0))
    for eachline in sort:
        manfaclist.append(eachline[0:3])
        damaged_column.append(eachline[3])
        device_list.append(eachline[0:2])
#pulling data from the price csv file by sorting ID
with open("PriceList.csv") as pricelist:
    pl = csv.reader(pricelist,delimiter=",")
    mort = sorted(pl,key= operator.itemgetter(0))
    for pline in mort:
        price_list.append(pline[1])
#pulling data from the service dates csv file by sorting ID
with open("ServiceDatesList.csv") as sdlist:
    sl = csv.reader(sdlist,delimiter=",")
    bort = sorted(sl,key = operator.itemgetter(0))
    for dline in bort:
        service_date.append(dline[1])
#creating list for previous items in order by ID
for x in range(0,len(manfaclist)):
    manfaclist[x].append(price_list[x])
for x in range(0,len(manfaclist)):
    manfaclist[x].append(service_date[x])
for x in range(0,len(manfaclist)):
    manfaclist[x].append(damaged_column[x])
#creating lists for the device types in the inventory
for x in range (0,len(device_list)):
    device_list[x].append(price_list[x])
    device_list[x].append(service_date[x])
    device_list[x].append(damaged_column[x])

# Creating a csv file for full inventory and sorting by manufacturer
fill = sorted(manfaclist,key=operator.itemgetter(1))

with open("FullInventory.csv","w",newline="") as tfi:
    
    csv_writer= csv.writer(tfi)
    csv_writer.writerows(fill)
#Creating a csv file for items that are laptops

for laptop in range(0,len(manfaclist)):
    if manfaclist[laptop][2] == "laptop":
        laptop_list.append(device_list[laptop])

with open ("LaptopInventory.csv","w",newline="") as tll:
    lap_writer = csv.writer(tll)
    lap_writer.writerows(laptop_list)
#Creating a csv file for items that are towers
for tower in range(0,len(manfaclist)):
    if manfaclist[tower][2] == "tower":
        tower_list.append(device_list[tower])
with open ("TowerInventory.csv","w",newline="") as ttl:
    tow_writer = csv.writer(ttl)
    tow_writer.writerows(tower_list)
#Creating csv for items in inventory that are phones
for phone in range(0,len(manfaclist)):
    if manfaclist[phone][2] == "phone":
        phone_list.append(device_list[phone])
        
with open ("PhoneInventory.csv","w",newline="") as tpl:
    pho_writer = csv.writer(tpl)
    pho_writer.writerows(phone_list)

#Creating csv file for items that have status of damaged and in order of price
for damaged in range(0,len(manfaclist)):
    if manfaclist[damaged][5] == "damaged":
        damaged_list.append(manfaclist[damaged][0:5])
# sorting the csv data in price reverse so its highest to lowest
dill = sorted(damaged_list,reverse= True,key=operator.itemgetter(int(3)))
with open("DamagedInventory.csv","w",newline="") as dml:
    dam_writer = csv.writer(dml)
    dam_writer.writerows(dill)
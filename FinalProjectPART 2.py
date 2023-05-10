#Joshua Perez
#ID:1837170
#importing csv and datetime module for later use 
import csv
from datetime import datetime
#creating functions to specifically target certain columns in csv files
def first_row_sort(row):
    return row[0]
def get_price(item):
    return(int(item[3]))
#Creating lists that will filter input string items to determine if they are valid or not
key_words=[]
man_list = []
#These lists will be appended with specific data that will be combined together later on.
price_list = []
dates_list =[]
man_dam = []
#opening all the given files to begin extracting data
with open('ManufacturerList.csv', 'r') as file:
    reader = csv.reader(file)
    #Sorting all rows by ID so the all line up in later combination
    sorted_rows = sorted(reader, key=first_row_sort)
    for line in sorted_rows:
      #appending data to different lists
        man_list.append(line[0:3])
        man_dam.append(line[3])
        key_words.append(line[1])
        key_words.append(line[2])
with open('PriceList.csv', 'r') as file:
    reader = csv.reader(file)
    sorted_rows = sorted(reader, key=first_row_sort)
    for row in sorted_rows:
        price_list.append(row[1])
with open('ServiceDatesList.csv', 'r') as file:
    reader = csv.reader(file)
    sorted_rows = sorted(reader, key=first_row_sort)
    for i in sorted_rows:
        dates_list.append(i[1])
  #Adding all the data to one list to be in a specific order but sorted
for x in range(0,len(man_list)):
    man_list[x].append(price_list[x])
for x in range(0,len(man_list)):
    man_list[x].append(dates_list[x])
for x in range(0,len(man_list)):
    man_list[x].append(man_dam[x])
    #creating csv file named "FullData.csv" to read information from 
with open('FullData.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(man_list)
    #Beginning the actual program by asking for the inquiry
inquiry = ''
while inquiry != "q":
    inquiry = input("What item are you looking for?:\n")
    #splitting the string to filter out unwanted words
    inq_split = inquiry.split()
    if inquiry == "q":
        break
    #These lists will hold and compare words from the inquiry
    passing_words=[]
    exact_item = []
    similar_item =[]
    other = []
    #Adding any words from the manufacturer and device column 
    for item in inq_split:
        if item in key_words:
            passing_words.append(item)
        else:
            other.append(item)
    #reading the data and comparing lists to see what is registered
    with open ("FullData.csv","r") as csv_file:
        csv_reader = csv.reader(csv_file)
        #if first round of requirements are not met then the item does not exist 
        if len(passing_words) == 0 or len(passing_words)>2 or len(passing_words)== 1 and len(other)>0:
            print("No such item in inventory")
        else:
            for line in csv_reader:
              #adding all of the conditions such as damaged, past service date and if the combination exists
                date_str = line[4]
                date_obj = datetime.strptime(date_str, '%m/%d/%y')
                #creating data for devices that are similar but have different manufacturers
                if line[1] != passing_words[0] and line[2]==passing_words[1] and date_obj > datetime.now() and line[5] != "damaged":
                    similar_item.append(line)
                if line[1] == passing_words[0] and line[2] == passing_words[1] and date_obj > datetime.now() and line[5] != "damaged":
                    exact_item.append(line)
            #if all else is damaged or past service date, then item does not exist
            if not exact_item:
                print("No such item in inventory")
            elif len(similar_item) == 0:
              #returning the item with the highest price if there are more than none available
                max_price = max(exact_item, key = get_price)
                print(f"Your item is ID:{max_price[0]}, Manufacturer:{max_price[1]}, Device:{max_price[2]}, Price:${max_price[3]}")
            else:
                max_price = max(exact_item, key = get_price)
                op = max_price[3]
                 #returning the item with the highest price if there are more than one available amnd reccomending the next similar item with closest price
                print((f"Your item is ID:{max_price[0]}, Manufacturer:{max_price[1]}, Device:{max_price[2]}, Price:${max_price[3]}"))
                diffs = []
                #using the absolute value fucntion to get any items closest price to the one that is found
                for row in similar_item:
                    diff = abs(int(op) - int(row[3]))
                    diffs.append(diff)
                min_diff = min(diffs)
                min_index = diffs.index(min_diff)
                print(similar_item[min_index][2])
                print(f"Perhaps you would enjoy this similar item ID:{similar_item[min_index][0]}, Manufacturer:{similar_item[min_index][1]}, Device: {similar_item[min_index][2]},Price: ${similar_item[min_index][3]}")

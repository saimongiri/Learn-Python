# List

mylist = ['apple' , 'banana' , 'Cherry'] # list are changeable and allows duplicates
print(mylist)
 
 # List items are indexed from 0

 #list length
print(len(mylist))

# list type
print(type(mylist))

# List Constructor

thislist = list(("mango","Orange"))#note the double rounded brackets
print(thislist)

# Access Items

print(mylist[1])

print(mylist[-1]) #negative indexing

print(mylist[1:2]) # range of indexes

# Check item in list

if "apple" in mylist:
    print("Apple is in mylist")


#Change List items
thislist[1]= 'Watermelon'
print(thislist[1])

#Add item in list

thislist.append(mylist)
print(thislist)
thislist.extend(mylist)
print(thislist)

#insert item
thislist.insert(3,'Orange')
print(thislist)

# Remove item from list
thislist.remove('mango')
print(thislist)

# Remove the specified index
thislist.pop(2)

#clear the list
thislist.clear()
print(thislist)

# delete complete list
del thislist


#Loop List

for x in mylist:
    print(x)

# Loop through the index numbers

for i in range(len(mylist)):
    print(mylist[i])


# Using while loop
k=0
while k < len(mylist):
    print(mylist[k])
    k=k+1


# Sort list
mylist.sort()
print(mylist)

# Sort decending
mylist.sort(reverse = True)
print(mylist)

# Case insensitive sort
mylist.sort(key= str.lower)
print(mylist)

# Reverse
mylist.reverse()
print(mylist)


# This is used for coding of basic python

print(" Hello World!")

# Variables (Python has no command for declaring a variabel)

x=5 # It automatically detect it as the integer variable
print(type(x)) # type function is used for getting type of variables, list or other datasets

y = "John" # y is string

z = 0.10 # z is float

# Casting 

x = str(3) # x will be string '3'
y= int(3)
z= float(3)

print(x , y , z)

# Variable names are case sensitive

a = 4
A = "Saimon"
# A will not overwrite a
print( a , A)

# Global Variable

name = "Saimon"
surname = "Giri"

def introduction():
    print("Hi, I am "+name+" "+surname+".")

introduction()
x = 5
y = 10

# Arithimetic Operators
print("Addition : ",x+y)
print("Subtraction : ",x-y)
print("Multiplication : ",x*y)
print("Division : ",float(x/y))
print("Modulus : ",x%y)
print("Exponential : ",x**y)
print("Floor Division : ",x//y)

# Assignment Operator

a=3 # assign value to a
print("a=3",a)
a+=3 # a=a+3
print("a+=3 : ",a)
a-=3 # a=a-3
print("a-=3 : ",a)

a*=3 # a=a*3
print("a*=3 : ",a)
a/=3 # a=a/3
print("a/=3 : ",a)

a%=3 # a=a+3
print("a%=3 : ",a)
a//=3 # a=a//3
print("a//=3 : ",a)

a**=3 # a=a**3
print("a**=3 : ",a)


# Comparison Operator

x = int(input("Enter first number : "))
y = int(input("Enter another number :"))

if x==y: #equal
    print("X and Y are equals")
if x!=y : # not equal
    print("x and y are not equal")
if x>y : # greater than
    print("x is greater than y")
if x<y : #less than
    print("y is greater than x")
if x>=y: # greater than and equal
    print(" X is greater or equal to y")
if x<=y: # less than or equal
    print("y is less than or equal to x")


# Logical Operator

if x< 5 and y>10 : # return true if both conditions are satisfied
    print(" x is less than 5 and y is greater than 10")

if x<5 or y>10: # return true if one of the condition is satisfied
    print("true")
else:
    print("false")

if not(x<5 and y>10): # reverse the result
    print("true")
else:
    print("False")


# Remaining 
# 1. Bitwise
# 2.Membership
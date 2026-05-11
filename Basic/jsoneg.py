# importing the package from bulit-in package
import json

# Convert from JSON to Python

#Some Json
x= '{"Name":"Saimon","age":19,"city":"Bhaktapur"}'

#parse x
y = json.loads(x)

# the result in python dictionary
print(y)

#Convert Python to JSON

a= y # copying dictionary to a

b = json.dumps(a)

print(b)
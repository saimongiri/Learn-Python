try :
    x=5
    y=0
    print("x :",x)
    print("y :",y)
    division = x/y
except ZeroDivisionError:
    print("division by 0")
except:
    print("Exception occured")
else:
    print("Nothing")
finally:
    print("wrong")

# Raise an exception

if x==5:
    raise Exception("Sorry , Divider is equal to zero")
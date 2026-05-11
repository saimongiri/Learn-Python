class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    # Self parameter is a reference to the current instance of the class
p = person('Saimon','Giri')
print("Hi, I am "+p.firstname+" "+p.lastname+".")
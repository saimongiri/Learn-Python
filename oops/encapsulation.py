class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age
    

p = Person("Saimon" , 19)
p.get_age()
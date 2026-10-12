class employee:
    language="python"
    salary=10000 

    def __init__(self):
        print("This is constructor method") #dunder method which is automaticlly called when we create an object of the class

    def getname(self):
        print("name is:",self.name)

shyam=employee()
shyam.name="shyam"
shyam.getname()


# example of class attributes

ram=employee()
print(ram.name)
print(ram.language)
print(ram.salary)    

# example of instance attributes

shyam=employee()
shyam.name="shyam"
shyam.language="java"
shyam.salary=15000
print(shyam.name)
print(shyam.language)
print(shyam.salary)


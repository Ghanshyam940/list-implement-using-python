# dictionary is a collection of key-value pairs in Python.
# Each key is unique and is used to access the corresponding value.
# Dictionaries are defined using curly braces {} and can store various data types as 
# values, including numbers, strings, lists, and even other dictionaries.
# dictionaries are mutable, meaning that you can change their content after creation.



marks={
    "maths": 90,
    "science": 85,  
    "english": 88,
    "history": 92
}
print("The marks of the subjects are:", marks)
print(type(marks))  # This will print <class 'dict'> because marks is a dictionary
print("The marks in maths are:", marks["maths"])  # Accessing the value for the key 'maths'
print("The marks in science are:", marks["science"])  # Accessing the value for the key 'science'
print("The marks in english are:", marks["english"])  # Accessing the value for the key 'english'
print("The marks in history are:", marks["history"])  # Accessing the value for the key 'history'

replacement_marks = {
    "maths": 95
}
print("The updated marks in maths are:", replacement_marks["maths"])  # Accessing the updated value for the key 'maths'


print(marks["maths"])  # This will raise a TypeError because dictionaries are accessed using square brackets, not parentheses

marks.update({"maths": 95, "physics": 88})  # Updating the value for the key 'maths' and adding a new key-value pair
print("The updated marks are:", marks)

marks=marks.get("maths")  # Getting the value for the key 'maths'
print("The marks in maths are:", marks)  # This will print the value for the key 'maths'

marks=marks.pop("science")  # Removing the key-value pair for the key 'science'
print("The marks after removing science are:", marks)  # This will print the value for
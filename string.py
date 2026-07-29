name= "ghanshyam"
print("hello, " + name + "!")
print("The name is:", name)
print("The type of the name is:", type(name))

print("The name is alphanumeric:", name.isalnum())
print("The name is alphabetic:", name.isalpha())
length= len(name)
print("The length of the name is:", length)

print("The name in uppercase is:", name.upper())
print("The name in lowercase is:", name.lower())
print("The name with the first letter capitalized is:", name.capitalize())
print("The name with the first letter of each word capitalized is:", name.title())

sliced_name= name[1:4]
print("The sliced name is:", sliced_name)
namesort=name[-4:-1]
print("The sorted name is:", namesort)    

name=name.endswith("am")
print("The name ends with 'am':", name)
name=name.startswith("gh")
print("The name starts with 'gh':", name)

a="ram is my favourite friend"
replace=a.replace("ram","ghanshyam")
print(a)
print(replace)

x="python is my favourite subject"
y=x.find("favourite")
print(y)

paragraph="python is a programming language. python is easy to learn. python is used for web development, data analysis, artificial intelligence, and more."
count=paragraph.count("python")
print("The word 'python' appears", count, "times in the paragraph.")

word="python is a programming language\n python is easy to learn\n python is used for web development, data analysis, artificial intelligence, and more."
print(word)

name=input("Enter your name: ")
print("Hello, " + name + "!")  # Concatenation
print(f"Hello, {name}!")

from os import replace

letter="""Dear <|NAME|>,
You are selected!
Date: <|DATE|>"""
print(letter.replace("<|NAME|>", "ghanshyam").replace("<|DATE|>", "1/1/2024"))
print(letter.replace("<|DATE|>", "1/1/2024"))

name="my   name is   ghanshyam   gaud"
x=name.find ("  ")
print(x)
replace=name.replace("  "," ")
print(replace)

detect=name.find("  ")
if detect==-1:
    print("No double spaces found.")
elif detect>=0:
    print("Double spaces found at index:", detect)

paragraph="python is a programming language. python is easy to learn. python is used for web development, data analysis, artificial intelligence, and more."
count=paragraph.count("python")
print("The word 'python' appears", count, "times in the paragraph.")

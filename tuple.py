# tuples are immutable sequences in Python,
# meaning that once a tuple is created, its elements cannot be changed, added, or removed.
# Tuples can contain elements of different data types, including integers, floats, strings, 
# and even other tuples.

a=(1,2,3,1,1,1,4,5,6,7.5,"abc",8,9,10)
print(type(a))
# a[1] = 20  # This will raise a TypeError because tuples are immutable

b=(1)
print(type(b))  # This will print <class 'int'> because it's not a tuple

b=(1,)
print(type(b))  # This will print <class 'tuple'> because it's a single-element tuple 

no=a.count(1)
print("The count of 1 in the tuple is:", no)

d=a.index(7.5)
print("The index of 7.5 in the tuple is:", d)

c=a[0:5]  # Slicing the tuple to get the first five elements
print("The sliced tuple is:", c)

e=(1, 2, 3, 4, 5)
f=(6, 7, 8, 9, 10)
combined_tuple = e + f  # Concatenating two tuples
print("The combined tuple is:", combined_tuple)

g=(1, 2, 3, 4, 5)   
repeated_tuple = g * 3  # Repeating the tuple three times
print("The repeated tuple is:", repeated_tuple)

my_tuple = (1, 2, 3, 4, 5)
print("The original tuple is:", my_tuple)
print(2 in my_tuple)  # Checking if 2 is in the tuple
print(6 in my_tuple)  # Checking if 6 is in the tuple

length = len(my_tuple)  # Getting the length of the tuple
print("The length of the tuple is:", length)



marks=[]
f1=int(input("Enter the marks of subjects: "))
marks.append(f1)
f2=int(input("Enter the marks of subjects: "))
marks.append(f2)
f3=int(input("Enter the marks of subjects: "))
marks.append(f3) 
f4=int(input("Enter the marks of subjects: "))
marks.append(f4)
f5=int(input("Enter the marks of subjects: "))
marks.append(f5)
print("The marks of the subjects are:", marks)

sorted_marks = sorted(marks)  # Sorting the list of marks
print("The sorted marks are:", sorted_marks)

sum the numbers in the tuple

a=(23,45,63,52)
total = sum(a)
print("The sum of the numbers in the tuple is:", total)

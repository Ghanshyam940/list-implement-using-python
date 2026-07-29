# set is a collection data type in Python that is unordered, mutable,and does not allow
# duplicate elements. It is defined using curly braces {} or the set() constructor.
# Sets are commonly used for membership testing, removing duplicates from a sequence,
#  and performing mathematical operations like union, intersection, and difference.

# a={1, 2, 3, 4, 5}

# len_a=len(a)
# print("Length of set a:", len_a)

# type_a=type(a)
# print("Type of set a:", type_a)

# replace={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a)
# print(replace)
# # Sets are unordered, so indexing is not supported
# # index=replace.index(5)
# # print(index)

# b={6, 7, 8, 9, 10}
# union_set=a.union(b)
# print("Union of a and b:", union_set)

# intersection_set=a.intersection(b)
# print("Intersection of a and b:", intersection_set)

# remove_set=a.difference(b)
# print("Difference of a and b:", remove_set)

# pop=a.pop()
# print("Popped element from a:", pop)

# c={}
# print("Type of c:", type(c))  # This will print <class 'dict'> because {} creates an empty dictionary, not a set.

# d=set()
# print("Type of d:", type(d))  # This will print <class 'set'>

# f={1, 2, 3, 4, 5 ,"Hello", 3.14, True}
# print("Set f:", f)
# print("Type of f:", type(f))  # This will print <class 'set'>

# f.add("World")
# print("Set f after adding 'World':", f)

# f.remove(3.14)
# print("Set f after removing 3.14:", f)

# clear_set=f.clear()
# print("Set f after clearing:", f)  # This will print an empty set: set

# add_set=f.add(42)
# print("Set f after adding 42:", f)  # This will print the set with 42 added: {42}

# upper_set=f.update({11, 22, 33})
# print("Set f after updating with {11, 22, 33}:", f)

# lower_set=f.update([44, 55, 66])
# print("Set f after updating with [44, 55, 66]:", f)   
# # python list can store any data type, including integers, strings,and even other lists.
# # Lists are mutable, meaning you can change their content without changing their identity.
# # Tuples, on the other hand, are immutable and cannot be changed after they are created.

friends = ["Alice", "Bob", 7, 3.76,True, "Charlie"]
print( friends)

print("The type of the friends list is:", type(friends))
print(friends[0])  # Accessing the first element
print(friends[1])  # Accessing the second element
friends[0] = "David"  # Modifying the first element
print("After modification, the friends list is:", friends)
print(friends[0])
print(friends[0:3])  # Slicing the list to get the first three elements

sorted_friends = sorted(friends, key=str)  # Sorting the list (converting all elements to strings for comparison)
print("The sorted friends list is:", sorted_friends)

reversed_friends = list(reversed(friends))  # Reversing the list
print("The reversed friends list is:", reversed_friends)

appended_friends = friends + ["Eve", "Frank"]  # Appending new elements to the list
print("After appending new friends, the friends list is:", appended_friends)

inserted_friends = friends[:2] + ["Grace"] + friends[2:]  # Inserting a new element at a specific position
print("After inserting a new friend, the friends list is:", inserted_friends)

popped_friend = friends.pop(1)  # Removing an element by index
print("After popping a friend, the friends list is:", friends)

removed_friend = friends.remove("Charlie")  # Removing an element by value
print("After removing a friend, the friends list is:", friends)




# 1. Creating an empty list called my_list
my_list = []
print("Empty list:", my_list)

# 2. Appending the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending elements:", my_list)

# 3. Inserting the value 15 at the second position in the list
my_list.insert(1, 15)
print("After inserting 15 at position 1:", my_list)

# 4. Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

# 5. Removing the last element from my_list
my_list.pop()
print("After removing the last element:", my_list)

# 6. Sorting my_list in ascending order
my_list.sort()
print("After sorting in ascending order:", my_list)

# 7. Finding and printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of value 30 in my_list is: {index_of_30}")
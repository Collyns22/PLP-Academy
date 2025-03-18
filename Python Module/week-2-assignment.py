# 1. creating an empty list
my_list = []

# 2. Appending 10,20,30,40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# 3. Inserting the value 15 at the second position of the list
my_list.insert(1, 15)
print(my_list)

# 4. Extending  my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

# 5. Removing the last element from the list
my_list.pop()
print(my_list)

# 6. Sorting the list in ascending order
my_list.sort()
print(my_list)

# 7. Finding and printing the index of the value 30 in the sorted list
print(my_list.index(30))
print(my_list)
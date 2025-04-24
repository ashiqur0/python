#### Join List ####

# Join Two List
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Append list2 to list1
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for x in list1:
    list1.append(x)
print(list2)

# By extend()
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
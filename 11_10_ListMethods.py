#### List Methods ####

# append() method
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

# clear() method
list1 = [2, 3, 4]
list1.clear()
print(list1)

# copy() method
list1 = ['a', 'b', 'c']
list2 = []
list2 = list1.copy()
print(list2)

# count() method
list1 = [1, 2, 4, 5, 1]
x = list1.count(1)  # It shows a specific value how many times present
print(x)

# extend() method
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# index() method
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('cherry'))   # return index of first specific element

# insert() method
num = [1, 2, 3]
num.insert(1, 100)
print(num)

# pop() method
num = [2, 3, 4]
num.pop(0)
print(num)  # [3, 4]
num.pop()
print(num)  # [3]

# remove() method
num = [1, 2, 3]
num.remove(1)
print(num)

# reverse() method
num = [2, 3, 1, 9, 4]
num.reverse()
print(num)

# sort() method
num = [4, 3, 5, 2, 6, 1, 8, 9, 7, 0]
num.sort()
print(num)
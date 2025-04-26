#### Join Set ####

#### Union ####
# union() method
fruits1 = {'apple', 'banana', 'cherry'}
fruits2 = {'banana', 'orange', 'kiwi'}
fruits3 = fruits1.union(fruits2)
print(fruits3)

# | operator instead of union() method
fruits3 = fruits1 | fruits2
print(fruits3)

# Join Multiple Set
set1 = {'apple', 'banana', 'cherry'}
set2 = {1, 2, 3}
set3 = {'a', 'b', 'c'}
set4 = {'John', 'Jack'}
myset = set1.union(set2, set3, set4)
print(myset)

# Join multiple set using | (bitwise or) operator
myset2 = set1 | set2 | set3 | set4
print(myset2)

# Update
fruits1 = {'apple', 'banana', 'cherry'}
fruits2 = {'cherry', 'orange', 'kiwi'}
fruits1.update(fruits2)
print(fruits1)

# Intersection with intersection() method : It will not change any set
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.intersection(set2)
print(set3)

# Intersection with & operator
set4 = set1 & set2
print(set4)

# Intersection with intersection_update() method : it will update the set
set1.intersection_update(set2)
print(set1)

# Difference
set1 = {'apple', 'banana', 'cherry'}
set2 = {'apple', 'a', 'b'}
set3 = set1.difference(set2)
print(set3)

set4 = set1 - set2      # set difference with - operator
print(set4)

set1.difference_update(set2)
print(set1)

# Symmetric Difference
set1 = {'apple', 'banana', 'cherry'}
set2 = {'apple', 'a', 'b'}
set3 = set1.symmetric_difference(set2)
print(set3)

set4 = set1 ^ set2      # symmetric difference with ^ (XOR) operator
print(set4)

set1.symmetric_difference_update(set2)
print(set1)
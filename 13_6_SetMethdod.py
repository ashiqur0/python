#### Set Method ####

# add() method : Add an elements to the set
fruits = {'apple', 'banana'}
fruits.add('cherry')
print(fruits)

# clear() method : Clear all the elements from a set
fruits.clear()
print(fruits)

# copy() method : Returns a copy of the set
set1 = {1, 2, 3}
set2 = set1.copy()
print(set2)

# difference() method : Returns the elements from the first set that are not present in second set
set1 = {1, 2, 3}
set2 = {2, 4, 5}

set3 = set1.difference(set2)
print(set3)

set4 = set1 - set2  # - operator is same as difference method
print(set4)

# difference_update() method : remove the item from the set that are also present in another specified set
set1.difference_update(set2)
print(set1)

set1 -= set2        # -= operator perform same as difference_update() method
print(set1)

# discard() method : remove a specific element form a set
set1 = {1, 2, 3}
set1.discard(1)
print(set1)

# intersection() method : & Returns a set that intersection of two other set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.intersection(set2)
print(set3)

set4 = set1 & set2      # The & operator performs the same
print(set4)

# intersection_update() method : &=
set1.intersection_update(set2)
print(set1)

set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
set1 &= set2            # &= operator perform the same
print(set1)

# isdisjoint() method : returns wheter sets have a intersection or not
x = set1.isdisjoint(set2)
print(x)

# issubset() method : <= returns a set is subset with another or not
set1 = {'a', 'b', 'c'}
set2 = {'a', 'b'}
x = set1.issubset(set2)
print(x)

y = set1 <= set2        # <= operator perform as same
print(y)

z = set1 < set2     # < : returns all the elements of a set is presents in another sets or not
print(z)

# issuperset(), >=
set1 = {1, 2, 3}
set2 = {2, 3, 4}
x = set1.issuperset(set2)
print(x)

y = set1 >= set2
print(y)

z = set1 > set2     # returns all the elements of a set is present in this set or not
print(z)

# pop() method : remove an element from a set
set1 = {1, 2, 3}
set1.pop()
print(set1)

# remove() method : remove the specified method
set1 = {'a', 'b', 'c'}
set1.remove('a')
print(set1)

# symmetric_difference() method, ^ operator : return those elements that are not match
s1 = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}
x = s1.symmetric_difference(s2)
print(x)

y = s1 ^ s2
print(y)

# symmetric_difference_update() method, ^= operator: update the first set, with those elements that are not common
s1.symmetric_difference_update(s2)
print(s1)

s3 = {'c', 'd', 'e'}
s2 ^= s3
print(s2)

# union() method, | operator : join two set
x = {'a', 'b', 'c'}
y = {1, 2, 3}
z = x.union(y)
print(z)

w = x | y   # | (bitwise or) operator performs the same as update()
print(w)

# update() method :
x.update(y)
print(x)
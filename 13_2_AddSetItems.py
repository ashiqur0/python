#### Add Set Items ####

# Add Items : add() method used to add an element to a set
fruitSet = {'apple', 'banana', 'cherry'}
fruitSet.add('orange')
print(fruitSet)

# Add Sets : update() method is used to add a set to another set
set1 = {'apple', 'banana', 'cherry'}
set2 = {'orange', 'kiwi', 'melon'}
set1.update(set2)
print(set1)

# Add any Iterable: list, tuple to the set
mylist = ['apple', 'banana', 'cherry']
mytuple = ('orange', 'kiwi', 'melon')
myset = {'tomato', 'potato', 'onion'}
myset.update(mylist, mytuple)
print(myset)
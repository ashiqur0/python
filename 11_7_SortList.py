#### Sort List ####

# Sort List Alphanumerically
fruits = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
fruits.sort()
print(fruits)

# Sort The List Numerically
num = [50, 30, 90, 70, 40, 20, 10,60]
num.sort()
print(num)

# Sort Descending
num.sort(reverse=True)
print(num)

#### Customize Sort Function ####
# Sort The List Based on how close the number is to 50
def myfun(n):
    return abs(n - 50)

num = [100, 50, 65, 82, 23]
num.sort(key =  myfun)
print(num)

# Case Sensitive Sort
fruits = ['banana', 'Orange', 'Kiwi', 'cherry']
fruits.sort()
print(fruits)

# Case InSensitive Sort
fruits.sort(key = str.lower)
print(fruits)

# Reverse Order
fruits.reverse()       # Alphanumeric element এর ক্ষেত্রে reverse() function
print(fruits)
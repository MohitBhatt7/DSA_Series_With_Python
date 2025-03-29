# Arrays ----> Linear data structure that stores the elements of the same type type in contiguous memory location.

import array as ar
# Creating a integer array. 
arr = ar.array('i', [1,2,3,4,5])

# Accessing elements
print(arr[0])

# Inserting an element at index 2.
arr.insert(2, 10)
print(arr)

# Removing an element from array list.

arr.remove(arr[2]) # Using index.
print(arr)

arr.remove(2) # By using direct values present in array list.
print(arr)

# Travesing in an array.
for i in arr:
    print(i)
    
squared = [i ** 2 for i in arr]
print(squared)



Marks = ar.array('i',[10, 20, 30, 40, 50, 60, 70, 80, 90])
# Reversig the array.
Marks.reverse()
print(Marks)
# Print the maximum number.
print(max(Marks))
# Printing the minimum number.
print(min(Marks))

print(Marks.index(40))
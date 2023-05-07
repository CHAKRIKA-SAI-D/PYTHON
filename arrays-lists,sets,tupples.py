import array as arr
# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

#printing array as list
print(list(a),end=" ")

#printing array as set
print(set(a),end=" ")

#printing array as tupple
print(tuple(a),end=" ")
 
# creating an array with double type
b = arr.array('d', [2.5, 3.2, 3.3])
 
# printing original array
print("\nThe new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
    
    ##output:
The new created array is :  1 2 3 
[1, 2, 3] {1, 2, 3} (1, 2, 3) 
The new created array is :  2.5 3.2 3.3 

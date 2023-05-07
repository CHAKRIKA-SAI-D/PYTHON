
import array as arr
list1=[1,2,4,6]
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
b=arr.array('i',list1)
count=0
list2=[]
list3=a+b
print(list(list3))
for i in range(len(list3)):
    for j in range(len(list3)):
        if list3[i]==list3[j]:
            count=count+1
    list2.append(count)
    count=0
print(list2)
print(list(zip(list(list3),list2)))

##output:
[1, 2, 3, 1, 2, 4, 6]
[2, 2, 1, 2, 2, 1, 1]
[(1, 2), (2, 2), (3, 1), (1, 2), (2, 2), (4, 1), (6, 1)]

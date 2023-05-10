#numpy
import numpy as np
r=int(input())
c=int(input())
li=list(map(int,input().split()))
matrix=np.array(li).reshape(r,c)
print(matrix)
output:
2
2
1 2 3 4
[[1 2]
 [3 4]]


#addition with numpy
import numpy as np
r=int(input())
c=int(input())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
matrix1=np.array(list1).reshape(r,c)
matrix2=np.array(list2).reshape(r,c)#here reshape is changing the list to required matrix
add=np.add(matrix1,matrix2)#.add will take two arguments
print(add)
output:
2
2
1 1 1 1
2 2 2 2
[[3 3]
 [3 3]]


#mutiplilcation using numpy
import numpy as np
r=int(input("enter rows of first matrix: "))
c=int(input("enter column of first or rows of second matrix:"))
q=int(input("enter column of second matrix: "))
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
matrix1=np.array(list1).reshape(r,c)
matrix2=np.array(list2).reshape(c,q)#here reshape is changing the list to required matrix
mul=np.matmul(matrix1,matrix2)#.matmul will take two arguments
print(mul)
output:
enter rows of first matrix: 2
enter column of first or rows of second matrix:2
enter column of second matrix: 2
1 0 0 1
2 2 2 2
[[2 2]
 [2 2]]

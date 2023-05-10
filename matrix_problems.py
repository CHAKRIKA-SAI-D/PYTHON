#creating a matrix
r=int(input())
c=int(input())
matrix=[]
a=[]
for i in range(r):
  for j in range(c):
    a.append(int(input()))
  matrix.append(a)
for i in range(r):
  for j in range(c):
    print(matrix[i][j],end=" ")
  print()
output:
2
2
2
2
2
2
2 2 
2 2 


#addtion of matrix
r=int(input())
c=int(input())
matrix1=[]
matrix2=[]
a=[]
b=[]
print("enter the elements of matrix 1: ")
for i in range(r):
  for j in range(c):
    a.append(int(input()))
  matrix1.append(a)
print("enter the elements of matrix 2: ")
for i in range(r):
  for j in range(c):
    b.append(int(input()))
  matrix2.append(b)
for i in range(r):
  for j in range(c):
    print(matrix1[i][j],end=" ")
  print()
for i in range(r):
  for j in range(c):
    print(matrix2[i][j],end=" ")
  print()
for i in range(r):
  for j in range(c):
    print(matrix1[i][j]+matrix2[i][j],end=" ")
  print()

  output:
2
2
enter the elements of matrix 1: 
1
1
1
1
enter the elements of matrix 2: 
2
2
2
2
1 1 
1 1 
2 2 
2 2 
3 3 
3 3 


#multiplication
r=int(input("enter the size of rows of first matrix : "))
c=int(input("enter the size of columns of first matrix"))
s=int(input("enter the size of rows of second matrix : "))
p=int(input("enter the size of columns of second  matrix"))
if c!=s:
  print("invalid sizes")
else:
  matrix1=[]
  matrix2=[]
  matrix3=[]
  a=[]
  b=[]
  print("enter the elements of matrix 1: ")
  for i in range(r):
    a=[]
    for j in range(c):
      a.append(int(input()))
    matrix1.append(a)
  print("enter the elements of matrix 2: ")
  for i in range(s):
    b=[]
    for j in range(p):
      b.append(int(input()))
    matrix2.append(b)
  for i in range(r):
    d=[]
    for j in range(p):
      e=0
      for k in range(c):
        e=e+(matrix1[i][k]*matrix2[k][j])
      d.append(e)
    matrix3.append(d)
  for i in range(len(matrix3)):
    z=matrix3[i]
    for j in range(len(z)):
      print(z[j],end=" ")
    print()
output:
enter the size of rows of first matrix : 2
enter the size of columns of first matrix2
enter the size of rows of second matrix : 2
enter the size of columns of second  matrix2
enter the elements of matrix 1: 
2
2
2
2
enter the elements of matrix 2: 
1
0
0
1enter the size of rows of first matrix : 2
enter the size of columns of first matrix2
enter the size of rows of second matrix : 2
enter the size of columns of second  matrix2
enter the elements of matrix 1: 
2
2
2
2
enter the elements of matrix 2: 
1
0
0
1
2 2 
2 2 
2 2 
2 2 


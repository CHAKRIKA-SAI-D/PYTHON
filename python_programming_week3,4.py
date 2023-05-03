

#Write a Python program to multiply all the items in a list
from functools import reduce
def mul(a,b):
  return a*b
list1=[]
n=int(input("enter the number of numbers: "))
print("enter {} elements: ".format(n))
for i in range(0,n):
  c=int(input())
  list1.append(c)
multiply=reduce(mul,list1)
print(multiply)

#Write a Python program to remove duplicates from a list.
def remove_duplicates(a):
  b=set(a)
  return b
list1=[]
n=int(input("enter the number of items : "))
print("enter {} items: ".format(n))
for i in range(0,n):
  c=int(input())
  list1.append(c)
c=remove_duplicates(list1)
print(list(c))

#Write a Python program to count the number of strings from a given list of strings such that the string length is 2 or more and the first and last characters are the same.
def count_number(a):
  count=0
  for i in range(0,len(a)):
    c1=a[i]
    if len(c1)>=2:
      if c1[0]==c1[len(c)-1]:
        count=count+1
  return count
list1=[]
n=int(input("enter the number of strings : "))
for i in range(0,n):
  c=input()
  list1.append(c)
count=count_number(list1)
print("the count of such items is ",count)

#Write a function called palindrome that takes a string argument and returnsTrue
#if it is a palindrome and False otherwise. Remember that you can use the built-in
#function len to check the length of a string
def palindrome(a):
  count=0
  for i in range(0,len(a)):
    if a[i]!=a[len(a)-i-1]:
      count=count+1
  if count==0:
    return True
  else:
    return False
a=input("enter the string ")
palindrome(a)

#Write a function called has_duplicates that takes a list and returns True if there
#is any element that appears more than once. It should not modify the original list.
def has_duplicates(a):
  count=0
  for i in range(0,len(a)):
    for j in range(0,len(a)):
      if a[i]==a[j]:
        count=count+1
    if count>=2:
      return True
    else:
      count=0
  return False
list1=[]
n=int(input("enter the number of strings : "))
for i in range(0,n):
  c=input()
  list1.append(c)
has_duplicates(list1)

#Remove the given word in all the places in a string
def remove_string(a,n):
  str3=""
  str2=a.split(n)
  for i in range(0,len(str2)):
    str3=str3+str2[i]
  return str3
a=input("enter the string: ")
n=input("enter the string to be removed : ")
remove_string(a,n)


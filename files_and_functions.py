#creating a file
f=open("file1.txt","wt")
data = "Hello welcome to Python Programming \npython programming lab"
f.write(data)
data=" \nwelcome to colab \n"
f.write(data)

#output:
20

#writing a file 
data2=" "
ch=' '
ch=input()
f.write(ch)
f.close()
f=open("file1.txt","rt")
data2= f.read()
print(data2)

#output:
it b
Hello welcome to Python Programming 
python programming lab 
welcome to colab 
it b

#Write a function that reads a file file1 and displays the number of words, number of vowels, blank
#spaces, lower case letters and uppercase letters
list1=["a","e","i","o","u"]
list2="AEIOU"
word=1
char=0
lines=1
vowels=0
caps=0
small=0
for i in data2:
  if i ==" ":
    word+=1
  elif i=="\n":
    lines+=1
  else:
    char+=1
    if i in list1 or i in list2:
      vowels+=1 
    if ord(i) in range(65,91):
      caps+=1
    if ord(i) in range(97,123):
      small+=1
print(vowels,word,lines,char,caps,small)

#output:
22 13 4 68 3 65


d=dict()
list1=data2.split()
for word in list1:
  if word in d:
    d[word]+=1
  else:
    d[word]=1
for key in d.keys():
  if d[key]==max(d.values()):
    print(key)
  #print(key," : ",d[key])
#print(max(zip(d.keys(),d.values())))

#output:
welcome
to

#merging files
a=open("1file.txt","wt")
data1=input()
a.write(data1)
b=open("2file.txt","wt")
data2=input()
b.write(data2)
a.close()
b.close()
c=open("3file.txt","wt")
a=open("1file.txt","rt")
data3=a.read()
b=open("2file.txt","rt")
data4=b.read()
data5=data3+data4
c.write(data5)
c.close()
c=open("3file.txt","rt")
data6=c.read()
print(data6)

#output:
HELLO CODER 
ENJOY THE CODE 
HELLO CODER ENJOY THE CODE 

#functions
def file(n):
  fp=open("file-1.txt","wt")
  fp.write(n)
  fp.close()
  fp=open("file-1.txt","rt")
  data=fp.read()
  print(data)
n=input("enter the text : ")
file(n)

#output:
enter the text : qwert
qwert

#palindrome
def palindrome(n):
  for i in range(len(n)):
    if n[i]==n[len(n)-i-1]:
      return True
    else:
      return False
n=input("enter the string : ")
palindrome(n)

#output:
enter the string : madam
True


#number palindrome
def number(n):
  r=0
  num=n
  rem=0
  while(num>0):
    rem=num%10
    r=r*10 + rem
    num=num//10
  if r==n:
    return True
  else:
    return False
num=int(input("enter the number : "))
number(num)

#output:
enter the number : 12321
True


#collatz
def collatz(n):
  count=0
  while n!=1:
    if n%2!=0:
      n=3*n +1
      count=count+1
    else :
      n=n//2
      count=count+1
  return count
num=int(input("enter the number : "))
collatz(num)

#output:
enter the number : 9
19


#factorial
def factorial(n):
  prod=1
  while(n!=1):
    prod=prod*n
    n=n-1
  return prod
num=int(input("enter the number : "))
factorial(num)

#output:
enter the number : 5
120

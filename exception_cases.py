#exception cases
a=int(input("enter the number: "))
b=int(input("enter the number : "))
d=input("enter your name: ")
li=[1,2,3]
try:
  d
  c=a%b
  li[3]
  z=a+b+e
  a+d
except IndexError:
  print("INDEX ERROR OCCURED")
except ZeroDivisionError:
  print("zero division error occured")
except NameError:
  print("name error occured")
except TypeError:
  print("type error occured")
  
 #output:
enter the number: 1
enter the number : 0
enter your name: 
zero division error occured


#index error
li=[1,2,3]
try:
  li[3]
except IndexError:
  print("index error")
  
#output:
index error


#name error
name=input("enter your name: ")
try:
  name1
except NameError:
  print("name error")
  
 #output:
enter your name: wert
name error


#type error
a=2
b="hello"
try:
  a+b
except TypeError:
  print("type error")
else:
  print("no type error")#excutes when except wont work
finally:
  print("finished!!!")#always excutes
 
#output:
type error
finished!!!


#key error
dict1={
    "one":1,
    "two":2,
    "three":3
}
print(dict1)
try:
  dict1["zero"]
except:
  print("key not found")
  
  #output:
{'one': 1, 'two': 2, 'three': 3}
key not found



#method-1
a=int(input("enter the number : "))
b=int(input("enter the number : "))
print("a is {} and b is {}".format(a,b))
temp=b
b=a
a=temp
print("a is {} and b is {}".format(a,b))


output:
enter the number : 5
enter the number : 3
a is 5 and is 3
a is 3 and is 5

#method-2
a=int(input("enter the number : "))
b=int(input("enter the number : "))
print("a is {} and b is {}".format(a,b))
a=a+b
b=a-b
a=a-b
print("a is {} and b is {}".format(a,b))

output:
enter the number : 5
enter the number : 3
a is 5 and is 3
a is 3 and is 5

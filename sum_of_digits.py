num=int(input("enter the number:"))
a=num
sum1=0
while(a>0):
    r=a%10
    sum1=sum1+r
    a=a//10
print("the sum is {}".format(sum1))


output:
enter the number : 123
the sum is 6

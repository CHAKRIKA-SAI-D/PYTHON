num=int(input("enter the number : "))
a=num
num1=0
while(a>0):
    r=a%10
    num1=num1*10 +r
    a=a//10
if(num==num1):
    print("palindrome!!")
else:
    print("not a palindrome!!")
    
output:
enter the number : 12321
palindrome!!

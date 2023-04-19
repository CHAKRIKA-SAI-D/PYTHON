num=int(input("enter the number: "))
f0,f1=0,1
print(f0,f1,sep="\n")
num1=2
while(num1!=num):
    f2=f1+f0
    print(f2)
    f0=f1
    f1=f2
    num1=num1+1
    
    
   output:
    enter the number :5
      0
      1
      1
      2
      3

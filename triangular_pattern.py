num=int(input("enter the number : "))
a=num
for i in range(0,num):
    for j in range(0,i+1):
        print(a,end="")
    a-=1
    print("\n")
    
output:
   enter the number : 5
      5
      44
      333
      2222
      11111

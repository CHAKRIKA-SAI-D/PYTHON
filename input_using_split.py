a,b,c=[int(x) for x in input("enter three numbers: ").split()]
if (a>b and a>c):
    print(a,"is greater")
elif (b>a):
    print(b,"is greater")
else:
    print(c,"is greater")
    
output :
  enter three numbers : 1 5 2
  5 is greater

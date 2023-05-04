def hcfnaive(a, b):
	if(b == 0):
		return abs(a)
	else:
		return hcfnaive(b, a % b)

a = int(input("enter first number : "))
b = int(input("enter the seconf number: "))
print("The gcd of {} and {} is : ".format(a,b), end="")
print(hcfnaive(a,b))

#output:
enter first number : 60
enter the seconf number: 48
The gcd of 60 and 48 is : 12

import random
num=int(input("guess the number: "))
num2=random.randint(1,5)
while(num!=num2):
    print("better luck next time!")
    num=int(input("guess the number: "))
print("congrats")

output:
  guess the number: 5
  better luck next time!
  guess the number: 3
  congrats
  
  

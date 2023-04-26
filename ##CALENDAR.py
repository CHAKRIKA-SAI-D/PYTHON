import calendar  
year = int(input ("Please enter the Year: ")) # Here, it will take the year  
month = int(input ("Please enter the month: "))    # Here, it will take the month  
      
    # Now, we will display the calendar  
print("The Calendar of: ", calendar.month(year, month)) 


output:
Please enter the Year: 2023
Please enter the month: 2
The Calendar of:     February 2023
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28

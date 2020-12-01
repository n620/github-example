year=int(input("enter a year:"))
if(year%4 and(year%400 or year%100)):
    print(year,"is not a leap year")
else:
    print(year,"is a leap year")

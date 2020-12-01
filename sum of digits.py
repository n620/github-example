num = int(input("enter a number:"))
sum=0
t = num
while t>0:
    digit=t%10
    sum=sum+digit
    t//=10
print(sum)

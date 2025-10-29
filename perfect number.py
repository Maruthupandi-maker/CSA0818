number=int(input("enter the number "))
sum=0
for i in range (1,number):
    if (number%i==0):
        sum=sum+i
        print(sum)
if (sum==number):
    print("{} is a perfect number".format(number))
else:
   print("{} is a not perfect number".format(number))

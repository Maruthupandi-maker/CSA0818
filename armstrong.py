Num=int(input("Enter The Number "))
Sum=0
Temp=Num
while Temp>0:
    Digit=Temp%10
    Sum+=Digit**3
    Temp=Temp//10
if Sum==Num:
    print("Armstrong Number")
else:
    print("Not A Armstrong Number")

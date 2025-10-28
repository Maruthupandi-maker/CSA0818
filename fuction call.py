def calsqr():
    print("1.calculate square ")
    n=int(input("Enter the number:"))
    s=n**2
    return s
print(calsqr())    
def celtofah():
    print("2.celsius to fahrenheit")
    C=int(input("enter celsius:"))
    F=(C*(5/9))+32
    print("the farhrenheit is ",C)
celtofah()
def areacircle():
    print("3.area of circle")
    r=float(input("enter radius:"))
    A=3.14*r*r
    print("area of the circle:",A)
areacircle()
def maxnum():
    print("4.max number")
    a=int(input("enter thr first number:"))
    b=int(input("enter the second number:"))
    return(max(a,b))
print(maxnum())

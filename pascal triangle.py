#pascal triange
r=int(input("Enter the rows"))
for i in range(1,r+1):
    print("*"*i)
#inverted
r=int(input("Enter the rows"))
for i in range(r,0,-1):
    print("*"*i)
#pyramid
r=int(input("Enter number of rows"))
for i in range(1,r+1):
    print(" "*(r-i)+"*"*(2*i-1))
#inverted
r=int(input("Enter number of rows"))
for i in range(r+1,0,-1):
    print(" "*(r-i)+"*"*(2*i-1))
#diamond
r=int(input("enter number of rows:"))
for i in range(1,r+1):
    print(" "*(r-i)+"*"*(2*i-1))
for i in range(r-1,0,-1):
    print(" "*(r-i)+"*"*(2*i-1))

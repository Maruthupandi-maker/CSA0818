x=int(input("enter the number"))
y=[]
print("the factors of",x,"are:")
for i in range(1,x):
    if x%i==0:
        y.append(i)
print(y)
print("Number of factors:",len(y))
N=int(input("enter N value:"))
if N>len(y):
    print("invalid")
else:
    print("first",N,"factors:")
    for k in range(0,N):
        print(y[k],end=' ')

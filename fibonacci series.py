n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
if n>=0:
    print("Fibonacci sequence:")
    while count < n:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1

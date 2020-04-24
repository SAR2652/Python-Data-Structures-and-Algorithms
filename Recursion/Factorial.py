def factorial(n):
    if n < 0:
        print("Invalid Input!!!")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
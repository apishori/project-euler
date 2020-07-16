def evenFibonacciSum(n):
    if n < 2:
        return 0
    a = 0
    b = 2
    sum = 2
    while EFn(a, b) < n:
        c = EFn(a, b)
        a = b
        b = c
        sum += c
    return sum

def EFn(a, b): #recursive definition of even fibonacci number
    return (4 * b + a)

def main():
    print(evenFibonacciSum(4000000))

if __name__ == "__main__":
    main()

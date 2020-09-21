import math


def properDivisorSum(n):
    total = 1
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            total += i 
            if i != n//i:
                total += n//i
        i += 1
    return total

def amicableNumberSum(n):
    d = {}
    total = 0
    for i in range(1,n+1):
        pds = properDivisorSum(i)
        if d.get(pds) == i:
            print(f"{i} and {pds}")
            total += i + pds
        d[i] = pds
    return f"Sum of amicable numbers under {n} = {total}"

if __name__ == "__main__":
    print(amicableNumberSum(10000))

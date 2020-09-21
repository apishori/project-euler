import math

def smallestMultiple(n):
    factors = []
    multiple = 1
    for i in range(2,n+1):
        for x in factors:
            if i % x == 0:
                i //= x
        if i != 1:
            factors.append(i)
            multiple *= i
    return multiple

if __name__ == "__main__":
    print(smallestMultiple(20))

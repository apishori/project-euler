import math


def ThreeFiveMultipleSum(limit):
    if limit < 0:
        return 0
    
    #number of multiples of 3, 5, 15 below limit
    num3 = math.floor((limit-1)/3)
    num5 = math.floor((limit-1)/5)
    num15 = math.floor((limit-1)/15)

    # sum of multiples of 3, 5, 15 below limit
    sum3 = 3 * Tn(num3)
    sum5 = 5 * Tn(num5)
    sum15 = 15 * Tn(num15)

    #substract 15 multiple sum to avoid double count
    return int(sum3 + sum5 - sum15)

def Tn(n): #returns sum of natural numbers from 1 to n
    return (n * (n + 1)/2)

def main():
    print(ThreeFiveMultipleSum(10))
    print(ThreeFiveMultipleSum(1000))

if __name__ == "__main__":
    main()

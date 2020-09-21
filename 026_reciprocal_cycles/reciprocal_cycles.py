import math

def reciprocalCycle(n):
    
    return

def largestReciprocalCycle(n):
    maxCycle = 0
    for i in range(2, n+1):
        if not isTwoOrFiveMultipleOnly(i):
            maxCycle = max(maxCycle, reciprocalCycle(i))
    return maxCycle

if __name__ == "__main__":
    print(largestReciprocalCycle(1000))

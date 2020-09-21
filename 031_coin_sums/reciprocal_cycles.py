def helperCoinSums(coins, target, i):
    if(i < 0):
        return 0
    num = 0
    for val in range(int(target/coins[i])+1):
        remain = target - val * coins[i]
        if(remain == 0):
            num += 1
        elif(remain > 0):
            num += helperCoinSums(coins, remain, i-1)
    return num

def coinSums(coins, target):
    x = helperCoinSums(coins, target, len(coins)-1)
    return f"{x} combinations of {coins} coins = {target}"

if __name__ == "__main__":
    print(coinSums([1,2,5,10,20,50,100,200], 200))

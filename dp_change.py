# dynamic programming solution to change-making problem
import numpy as np

def makeChange(coin_vals,change,min_coins):
    for cents in range(change+1): # for
        # set coint_ct = to number of cents (assumes all coin_vals will have pennies)
        coin_ct = cents
        # consider all denominations less than the amount of change being computed currently
        for j in [c for c in coin_vals if c <= cents]:
            #print("coin_ct = ", coin_ct, "j = ", j)
            # if the min number of coins for the current cents minus a certain denomination
            # *value*, plus 1 *count* of these coins is better than the current best guess
            #print("is min_coins of[", cents, "minus", j, "] + 1 less than", coin_ct, "?")
            if min_coins[cents-j]+1 < coin_ct:
            #    print("yes")
                # set new guess for coin_ct
                coin_ct = min_coins[cents-j]+1
            #else:
            #    print("no")
        min_coins[cents] = coin_ct
        #print("min_coins = ", min_coins[0:cents+1])
    return min_coins[change]

test = makeChange([1,5,12],16,np.empty([20,1]))
print(test)

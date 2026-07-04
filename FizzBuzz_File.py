import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)

    outlist = np.arange(start, finish + 1, dtype=object)
    outlist[nums % 3 == 0] = "fizz"
    outlist[nums % 5 == 0] = "buzz"
    outlist[nums % 15 == 0] = "fizzbuzz"

    return(outlist)

import sys
import math
import numpy as np
import matplotlib.pyplot as plt

num_limit = int(sys.argv[1])


# works pretty fast until like 10 million
def is_prime(n):
    for i in range(3, math.ceil(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def prime_dists_as_fractions(n):
    dist_frac_sum = 0
    dfsumc = []
    logs = []
    diff = 0
    last_prime = 2
    for i in range(3, n, 2):
        if is_prime(i):
            frac = (i-last_prime)/last_prime
            dist_frac_sum += frac
            dfsumc.append(dist_frac_sum)
            logs.append(math.log(last_prime))
            last_prime = i
    diff = math.log(last_prime)-dist_frac_sum
    print(dist_frac_sum, math.log(n))
    return dfsumc, logs, diff

if __name__ == "__main__":
    dfsum, logs, diff = prime_dists_as_fractions(num_limit)
    print(diff)
    plt.xlabel("Nth prime number")
    plt.ylabel("Sum of fractions")
    plt.title("Fractional prime distance sum and logarithm of the primes (difference: ~{})".format(str(round(diff, 3))))
    plt.plot(dfsum, label="Fractional prime distance sum")
    plt.plot(logs, label="Natural logarithm from 1 to " + str(num_limit))
    plt.grid()
    plt.legend()
    plt.show()

# brute force solution
def isPrime(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

# better solution
def isPrime(n):

    if n <= 1:
        return False

    count = 0

    for i in range(1, int(n**0.5) + 1):

        if n % i == 0:
            count += 1

            if n // i != i:
                count += 1

    if count == 2:
        return True
    else:
        return False

# optimal solution using sqrt of n
def isPrime(n):

    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:
            return False

    return True

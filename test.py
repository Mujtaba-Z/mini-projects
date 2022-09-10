primes = ''
num = 3
while len(primes) < 10005:
    for i in range(2, num):
        if (num % i) == 0:
            break
        else:
            primes += str(num)
    num += 1
    print(primes)
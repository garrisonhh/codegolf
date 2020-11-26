# 64 chars; calculates true primes
# [print(n)for n in range(2,99)if sum(n%x<1for x in range(2,n))<1]

# 54 chars; calculates probable primes
[print(n)for n in range(2,99)if n==2or 2**(n-1)%n==1]

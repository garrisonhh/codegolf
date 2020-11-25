[print(x)for x in range(51)if sum(n%x<1for x in range(2,bin(x).count('1')))<1]
# evil
# [print(x)for x in range(51)if bin(x).count('1')&1]

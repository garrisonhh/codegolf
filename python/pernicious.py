[print(n)for n in range(2,51)if(lambda n:sum(n%x<1for x in range(2,n))<1&(n>1))(bin(n).count('1'))]

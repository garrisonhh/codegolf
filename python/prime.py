# [print(n)for n in[2,*range(3,99,2)]if 0x1129A64B4CB6F>>int((n-1)/2)&1] # this isn't the most golfed solution but god damn is it not hilarious
[print(n)for n in range(2,99)if sum(n%x<1for x in range(2,n))<1] # most golfed currently

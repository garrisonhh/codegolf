s=["▲"]
for i in 0,1,2,3:s=[s[j]+" "*(j*2+1)+s[j]for j in range(2**i)]+s
print('\n'.join(" "*(15-i)+s[-i-1]for i in range(16)))

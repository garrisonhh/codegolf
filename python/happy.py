h=lambda n,z=[]:1if n<2else(0if n in z else h(sum(int(x)**2for x in str(n)),z+[n]))
[print(x)for x in range(1,201)if h(x)]

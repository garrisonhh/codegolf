z=range(1,101)
[print(*[y for y in z if x%y<1])for x in z]

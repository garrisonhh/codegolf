r,p=range,print
for i in r(9):
 for y in r(-i,i+1):d=i-abs(y);p(" "*(9-d),*r(1,d+2),*r(d,0,-1),sep='')
 p()

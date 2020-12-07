# https://codegolf.stackexchange.com/questions/215468/find-distance-between-the-closest-3d-points
#f=lambda p:min(sum((a-b)**2for a,b in zip(x,y))**.5for x in p for y in p if x!=y)
f=lambda p:min(sum((a-b)**2for a,b in zip(x,y))**.5for x,y in zip(p,[p]*3)if x!=y)

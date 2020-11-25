x,h,v,d,s="█─│╱ "
p=println
for i=1:7
t=x*h^(i*4)*x
z=s^(i*4)
n=v*z*v
p(s^(i+1),t)
for j=0:i-1
p(s^(i-j),d,z,d,s^j,v)end
p(t,s^i,v,'\n',(n*s^i*v*'\n')^(i-1),n,s^i,x)
for j=i-1:-1:0
p(n,s^j,d)end
p(t)
p()end

# translates args
import sys
u="IVXLCDM_"
# for a in sys.argv[1:]:print(''.join((lambda x,z:(u[z+2]+u[z])*(x>8)+(u[z]*(x-5)+u[z+1])*(3<x<9)+u[z]*(x*(x<4)+(x==4)))(int(a[-i-1]),i*2)for i in range(len(a)))[::-1])


# prints 1-100
u="IVXLCD"
for a in map(str,range(101)):print(''.join((lambda x,z:u[z]*(x*(x<4)+(x==4))+(u[z+1]+u[z]*(x-5))*(3<x<9)+u[z:z+3:2]*(x>8))(int(a[-i-1]),i*2)for i in range(len(a)-1,-1,-1)))

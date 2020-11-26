o,f="IXCM_","VLD_"
n(x,d)->o[d]^((x<4)&1*x+(x==4||x==9))*f[d]^((3<x<9)&1)*o[d]^((5<x<9)&1*(x-5))*o[d+1]^((x>8)&1)
for a in ARGS
s,d="",length(a)
for c in a
s*=n(Int(c)-48,d)
d-=1
end
println(s)end

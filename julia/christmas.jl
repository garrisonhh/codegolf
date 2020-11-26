for i=3:9
t=[" "^(i-j)*"*"^(j*2-1)*'\n' for j=1:i]
println(t...,t[1])end

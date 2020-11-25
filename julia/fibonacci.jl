f=[0,1]
for i in 1:31
println(push!(f,f[i]+f[i+1])[i])end

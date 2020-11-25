for i=1:9,y=-i:i-1
d=i-abs(y)
println(" "^(9-d),1:d...,d-1:-1:1...)
end

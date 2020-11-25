for x=1:100
c="Fizz"^max(1-x%3,0)*"Buzz"^max(1-x%5,0)
println(c>"" ? c : x)end

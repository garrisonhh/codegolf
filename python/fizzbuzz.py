# 76
#f,b="Fizz","Buzz"
#for i in range(1,101):print([f+b,b,f,i][(i%3>0)+2*(i%5>0)])

# 67
#[print("FizzBuzz"[(x%3>0)*4:4+(x%5<1)*4]or x)for x in range(1,101)]

# 62
#for x in range(1,101):print("Fizz"*(x%3<1)+"Buzz"*(x%5<1)or x)

# 62
x=1
exec('print("Fizz"*(x%3<1)+"Buzz"*(x%5<1)or x);x+=1;'*100)

t=1,
exec("print(*t);t=1,*[t[i+1]+t[i]for i in range(len(t)-1)],1;"*20)

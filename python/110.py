n=100;z='0';j=''.join;s=z*n+"10";exec("print(j(' █'[c>z]for c in s[1:-1]));s=z+j(str(110>>int(s[i:i+3],2)&1)for i in range(n))+z;"*n)

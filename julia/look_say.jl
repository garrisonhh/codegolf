((t="1")->[(println(t);n=1;s="";l=length(t);[(j==l||t[j]!=t[j+1] ? (s*="$n"*t[j];n=1) : n+=1) for j=1:l];t=s) for i=1:20])()

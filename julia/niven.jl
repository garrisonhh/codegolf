println.(filter(x->x%sum(Int.(c-48 for c in"$x"))<1,1:100))

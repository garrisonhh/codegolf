import sys
sys.argv+=["01023213213"]
for r in 0,3,6:print(''.join(" _ |_||_|"[((490,288,242,434,312,410,474,290,506,442)[int(a)]>>j&1)*j]for a in sys.argv[1]for j in range(r,r+3)))

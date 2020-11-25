"""
import sys
for a in sys.argv[1:]:n=int(a);print(a+("th"*(10<n%100<20)or"st nd rd th".split()[min(n%10-1,3)]))
"""

import sys
for a in sys.argv[1:]:n=int(a);print(a+("st","nd","rd","th")[min(n%10-1+(10<n%100<20)*3,3)])

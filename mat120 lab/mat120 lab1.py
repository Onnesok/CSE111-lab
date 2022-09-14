# Find the minima and maxima of the following functions at a given interval
# 1. y= 9x 3 −7x 2 +3x+10 in the interval [-5, 6]

# 2. y= ln x [-5, 6]

# 3. y= sin x [-5, 6]

# 4. y= cos x [-5, 6]

# 5. y= tan x [-5, 6]


############################  Task 1  ###############################

from numpy import diff
import sympy
#from sympy import*          #### another way

x, y, z = sympy.symbols("X, y, z")
f = 2*x**3 + x**2 + 3*x + 5
res1 = sympy.diff(f, x)
res2 = sympy.diff(f, x, 2)
print(res1, "\n",res2)
print(f.subs(x, 4))
print(res2.subs(x, 4).evalf())

s = 3*x**2 + 4*x*y - z

res3 = sympy.diff(s, x, 2)
dif3 = 2*x+y+z
print(res3)
print(dif3.subs([(x, 1), (y,2), (z, 3)]))
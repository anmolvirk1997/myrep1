#creating ur own modules in file calc.py
print(__name__)
import calc as c
print(__name__)
print(c.add(2,3))
print(c.sub(4,3))
print(c.mult(11,3))
print(c.div(9,3))

import calc
print(__name__)         #name varible in main code prints main if name varible is mentioned
                        #in imported module in main program it prints name of module

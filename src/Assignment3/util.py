
import numpy as np
def avg(n,marks,name):
    for i in range(n):
        ls=marks[name]
        avg=np.average(ls)
        print(avg)
        return(avg)

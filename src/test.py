from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import time
from random import random

testlist = [random()*10, random()*10]

i = 1
while i < 5:
    testlist.append(random()*10)
    i += 1

for x in range(len(testlist)):
    print(testlist[x], end=" ")

#df = pd.DataFrame({'x': range(1,101), 'y': np.random.randn(100)*15+range(1,101), 'z': (np.random.randn(100)*15+range(1,101))*2 })
 
## Plot
#plt.plot( 'x', 'y', data=df, marker='o', color='c')
#plt.show()
#time.sleep(5)
#df = pd.DataFrame({'x': range(1,101), 'y': np.random.randn(100)*15+range(1,101), 'z': (np.random.randn(100)*15+range(1,101))*2 })
#plt.draw()

#def reprint():
#    plt.plot('x', 'y', data=df, marker='o', color='c')


#def main():



#if __name__ == "main":
#    main()
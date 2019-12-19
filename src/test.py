#from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import time
from random import random
from pylab import figure, axes, plot, title, show, legend, savefig


def graph_create(mylist, type):

    i = 1
    while i < 10:
        mylist.append(random())
        i += 1

    for x in range(len(mylist)):
        print(mylist[x], end=" ")

    figure(1, figsize=(12, 6))

    plot(mylist)
    title('Diversity of %s' %type, bbox={'facecolor': '0.8', 'pad': 5})
    legend()
    

    #show()  # Actually, don't show, just save to foo.png
    savefig('foo.png', bbox_inches='tight')

# graph_create([random(), random()], 'f1')

#df = pd.DataFrame({'x': range(1,101), 'y': np.random.randn(100)*15+range(1,101), 'z': (np.random.randn(100)*15+range(1,101))*2 })
 
# Plot
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
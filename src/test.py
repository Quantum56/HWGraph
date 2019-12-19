#from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import time
import os
from os import path
from random import random
from pylab import figure, axes, plot, title, show, legend, savefig, ylim
import math as m



def graph_create(mylist, type):

    if path.exists('foo.png'):
        os.remove("foo.png")

    for x in range(len(mylist)):
        print(mylist[x], end=" ")

    figure(1, figsize=(12, 6))

    ylim(top=1)
    plot(mylist)
    title('Frequency of %s' %type, bbox={'facecolor': '0.8', 'pad': 5})
    legend()
    

    #show()  # Actually, don't show, just save to foo.png
    savefig('foo.png', bbox_inches='tight')

def mathything(a1, muta1a2, muta2a1, a1a1fit, a1a2fit, a2a2fit, popsize, gens, randomness, ifdecreasing):
    if randomness == 'yes':
        godcoeff = 0.51
    else:
        godcoeff = 0

    population = popsize

    p = a1
    q = 1 - a1
    a1freqarr = [p]
    a2freqarr = [q]
    a1a1arr = []
    a1a2arr = []
    a2a2arr = []
    a1arr = []
    a2arr = []
    a1a1 = p*p
    a1a2 = 2 * p * q
    a2a2 = q*q
    a1a1arr.append(a1a1)
    a1a2arr.append(a1a2)
    a2a2arr.append(a2a2)
    i = 0
    while i < gens:

        bb = random()
        if bb <= 0.5:
            bb = 1
        else:
         bb = -1


        a1a1 = 2*p*q*muta2a1 + p*p*a1a1fit + godcoeff * bb * 1/population * random()
        a1a2 = p*p*muta1a2 + q*q*muta2a1 + 2*p*q*a1a2fit + godcoeff * bb * 1/population * random()
        a2a2 = 2*p*q*muta2a1 + q*q*a2a2fit + godcoeff * bb * 1/population * random()
        p = m.sqrt(abs(a1a1))
        q = m.sqrt(abs(a2a2))
        a1a1arr.append(a1a1)
        a2a2arr.append(a2a2)
        a1a2arr.append(a1a2)
        a1arr.append(p)
        a2arr.append(q)
        

        a1a1 = round(a1a1 * 10000) / 10000
        a1a2 = round(a1a2 * 10000) / 10000
        a2a2 = round(a2a2 * 10000) / 10000

        i += 1

        if ifdecreasing:
            population -= (population * ((1-a1a1fit) + (1-a1a2fit) + (1-a2a2fit)))
    print(population)
    return a1arr

arr = mathything(0.5, 0, 0, 0.97, 1.0, 1.0, 100, 100, "yes", True)

for x in range(len(arr)):
    print(arr[x], end=" ")
graph_create(arr, 'A1')

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
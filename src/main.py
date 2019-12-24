import pandas as pd
import numpy as np
import time
import os
from os import path
from random import random
from pylab import figure, axes, plot, title, show, legend, savefig, ylim
import math as m
from datetime import datetime
#import logging

def main():
    print("Hardy-Weinberg Equilibrium Simulation Program")
    print("(c) 2019 Zack Bartley\n\n")
    try:
        param1 = float(input("Please enter A1 initial frequency (leave blank for default): "))
    except ValueError:
        param1 = 0.5

    #if param1 == None:
    #    param1 = 0.5
    try:
        param2 = float(input("Enter a1 -> a2 mutation rate: (leave blank for 0): "))
    except ValueError:
        param2 = 0
    #if param2 == None:
    #    param2 = 0
    try:
        param3 = float(input("Enter a2 -> a1 mutation rate: (leave blank for 0): "))
    except ValueError:
        param3 = 0
    #if param3 == None:
    #    param3 = 0
    try:
        param4 = float(input("Enter a1a1 allele fitness: (leave blank for 1.0): "))
    except ValueError:
        param4 = 1.0
    #if param4 == None:
    #    param4 = 1.0
    try:
        param5 = float(input("Enter a1a2 allele fitness: (leave blank for 1.0): "))
    except ValueError:
        param5 = 1.0
    #if param5 == None:
    #    param5 = 1.0
    try:
        param6 = float(input("Enter a2a2 allele fitness: (leave blank for 1.0): "))
    except ValueError:
        param6 = 1.0
    #if param6 == None:
    #    param6 = 1.0
    try:
        param7 = float(input("Enter population size: (leave blank for inf): "))
    except ValueError:
        param7 = 100000
    #if param6 == None:
    #    param6 = 10000000
    try:
        param8 = float(input("Enter number of graphed generations (leave blank for 100): "))
    except ValueError:
        param8 = 100
    #if param8 == None:
    #    param8 = 100
    param9 = input("Enter if randomness desired: (y/n) ")
    if param9 == "n":
        param9 = "nn"
    elif param9 == "y":
        param9 = "yes"
    param10 = input("Indicate if population is decreasing (y/n) ")
    if param10 == "n":
        param10 = False
    elif param10 == "y":
        param10 = True
    else:
        param10 = False
    
    param11 = input("Indicate which graph is desired (a1, a1a1, a1a2, a2a2) ")
    if param11 == None:
        param11 = "a1"

    delta1 = datetime.now()

    arr = mathything(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11)
    # param1, param2, param3, param4, param5, param6, param7, param8, param9, param10
    # a1, muta1a2, muta2a1, a1a1fit, a1a2fit, a2a2fit, popsize, gens, randomness, ifdecreasing
    # arr = mathything(0.5, 0, 0, 0.97, 1.0, 1.0, 100, 100, "yes", True)

    delta2 = datetime.now()

    time = delta2 - delta1
    print("Delta: " + str(time))
    graph_create(arr, 'A1')

def graph_create(pointlist, type):

    ##tests with logger
    #logger = logging.getLogger('HWGraph')
    #hdlr = logging.FileHandler('/HWGraph.log')
    #formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #hdlr.setFormatter(formatter)
    #logger.addHandler(hdlr) 
    #logger.setLevel(logging.WARNING)

    if path.exists('foo.png'):
        os.remove("foo.png")

    #for x in range(len(pointlist)):
    #    logger.info(str(pointlist[x]))

    figure(1, figsize=(12, 6))

    ylim(top=1)
    plot(pointlist)
    title('Frequency of %s' %type, bbox={'facecolor': '0.8', 'pad': 5})
    legend()
    

    show()  # Actually, don't show, just save to foo.png
    #savefig('foo.png', bbox_inches='tight')

def mathything(a1, muta1a2, muta2a1, a1a1fit, a1a2fit, a2a2fit, popsize, gens, randomness, ifdecreasing, returnedarr):
    if randomness == 'yes':
        godcoeff = 0.51
    else:
        godcoeff = 0

    population = popsize

    p = a1
    q = 1 - a1
    a1a1arr = []
    a1a2arr = []
    a2a2arr = []
    a1arr = [p]
    a2arr = [q]
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
            population = round(population)
            #print(population)
    print("End population is: " + str(population) + " individuals")
    
    if returnedarr == "a1":
        return a1arr
    elif returnedarr == "a1a1":
        return a1a1arr
    elif returnedarr == "a1a2":
        return a1a2arr
    elif returnedarr == "a2a2":
        return a2a2arr
    else:
        return a1arr

if __name__ == '__main__':
    main()

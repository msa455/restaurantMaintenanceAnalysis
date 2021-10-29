# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 00:14:27 2021

@author: pmjum
"""

import random
import matplotlib.pyplot as plt

profits = {1:-2,20:-1.5,30:-1,40:-.5,50:0,75:1,90:2,99:3,100:5}
breakpoints = [1,20,30,40,50,75,90,99,100]

def rollMaintenance(profits,breakpoints):
    roll = random.randint(1,100)
    #print("rolled a ", roll)
    for point in breakpoints:
        if(roll <= point):
            return(profits[point])
        

def calculateMaintenance(numDays, profits, breakpoints, baseMaintenance=5, startingGold=100):
    totalProfit = 0
    for x in range(numDays):
        totalProfit += (baseMaintenance * rollMaintenance(profits, breakpoints))
        #print("new daily maintenance: ", totalProfit)
    return totalProfit

def runSims(numTrials, profits, breakpoints, numDays=7, baseMaintenance=5):
    profitResults = []
    for x in range(numTrials):
        profitResults.append(calculateMaintenance(numDays, profits, breakpoints, baseMaintenance))
    return profitResults

def getCounts(profitResults,returnList=True):
    resultVals = list(set(profitResults))
    resultCounts = [profitResults.count(val) for val in resultVals]
    if(returnList):
        return(resultVals,resultCounts)
    else:
        return {resultVals[i]:resultCounts[i] for i in range(len(resultVals))}

(resultVals,resultCounts) = getCounts(runSims(10000,profits,breakpoints))
plt.bar(resultVals,resultCounts)
plt.show()



# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:02:30 2021

@author: Patrick
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def getData(directory):
    functionDurations = dict()
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            fileData = getFileData(directory + file)
            functions = fileData.keys()
            for function in functions:
                if function in functionDurations.keys():
                    functionDurations[function].extend(calculateDurations(fileData[function]))
                else:
                    functionDurations[function] = calculateDurations(fileData[function])
    return functionDurations
        
    

'''
Get the data from the file as a dict of the columns
'''
def getFileData(fileName):
    with open(fileName, newline='') as csvfile:
        csvData = csv.reader(csvfile, delimiter=',')
        for row in csvData:
           columns = row
           break
    columns.remove('')  # First column is an index without a headding, remove from the list
    return pd.read_csv(fileName, usecols=columns).to_dict('dict')  


def calculateDurations(data):
    
    # Get it to a list first
    dataList = list()
    for i in data.keys():
        dataList.append(data[i])

    differences = list()

    # subtract the previous from the current (or discard if no good)
    for i in range(len(dataList)):
        element = dataList[i]
        
        if (i == 0) and (element > 0):
            differences.append(element)
        
        if i < (len(dataList) - 1):
            nextElement = dataList[i + 1]
            if (nextElement > 0) and (element > 0):
                difference = nextElement - element
                if difference > 0:
                    differences.append(difference)
    return differences
                    
            
        
def generatePlot(data, functionNames, title):
    plotFileName = title.replace(' ','')
    plotFileName = plotFileName.replace(',','')
    
    outputPath = 'graphs/'
    if (not os.path.exists(outputPath)):
        os.mkdir(outputPath)
    
    relevantData = list()
    for function in functionNames:
        relevantData.append(data[function])
        
    # Create a figure instance
    fig = plt.figure()
  
    # Create an axes instance
    ax = fig.gca()
  
    # Create the violinplot
    ax.violinplot(relevantData, vert = False)
    ax.set_yticks(np.arange(1, len(functionNames) + 1))
    ax.set_yticklabels(functionNames)
    ax.set_xlabel("Duration (μs)")      # Check the unit
    ax.set_title(title)
    plt.savefig(outputPath + plotFileName + '.jpg', format='jpg', dpi=1000,
                bbox_extra_artists=(), bbox_inches='tight')
    


if __name__ == '__main__':
    functions = ['reasoningCycle','sense','deliberate','act']
    
    directory = ['D:/Local Documents/Github/savi_profiling/results/ASynchGridPC/',
                 'D:/Local Documents/Github/savi_profiling/results/ASynchGridRPi/',
                 'D:/Local Documents/Github/savi_profiling/results/Car/',
                 'D:/Local Documents/Github/savi_profiling/results/MailAgent/',
                 'D:/Local Documents/Github/savi_profiling/results/SynchGrid/']
    name = ['Asynchronized Grid Agent, PC',
            'Asynchronized Grid Agent, RPi',
            'Autonomous Car Agent, PC',
            'Mail Agent, RPi',
            'Synchronized Grid Agent, PC']
    
    for i in range(len(directory)):
        data = getData(directory[i])
        generatePlot(data, functions, name[i])
  
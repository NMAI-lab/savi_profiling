'''
    Parsing from XML into CSV
'''

import os
import math

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

from lxml import etree


interestedFunctions = [
    'reasoningCycle',
    
    'perceive',
    'buf',
    'checkMail',
    'selectEvent',
    'relevantPlans',
    'applicablePlans',
    'selectOption',
    'applyFindOp',
    'selectAction',
    'applyExecInt',
]


inputDir = #<Put your Directory here>


outputPath = inputDir + '/Cumulative_Data'
if (not os.path.exists(outputPath)):
    os.mkdir(outputPath)

line = 1
df = pd.DataFrame(columns = interestedFunctions)

run = 1
while (True):
    runFile_p = inputDir + '/snapshot_' + str(run - 1) + '.xml'
    runFile = inputDir + '/snapshot_' + str(run) + '.xml'

    outputName = outputPath + '/Cumulative.csv'
    if (not os.path.exists(runFile)):
        print(runFile + " doesn't exist, aborting")
        break

    p = etree.XMLParser(huge_tree = True)
    doc_p = etree.parse(runFile_p, parser = p)
    doc = etree.parse(runFile, parser = p)

    rcNode_p = doc_p.find("//node[@methodName=\"reasoningCycle\"]")
    rcNode = doc.find("//node[@methodName=\"reasoningCycle\"]")
    if (rcNode_p == None):
        run += 1
        continue

    data = []
    for x in interestedFunctions:

        if (x == "reasoningCycle"):
            tempTime_p = int(rcNode_p.get("time"))
            tempTime = int(rcNode.get("time"))
        else:    

            temp_p = rcNode_p.find(".//node[@methodName='" + x + "']")
            temp = rcNode.find(".//node[@methodName='" + x + "']")
            if (temp == None):
                tempTime = 0
            else:
                tempTime = int(temp.get("time"))

            if (temp_p == None):
                tempTime_p = 0
            else:
                tempTime_p = int(temp_p.get("time"))


        timeDiff = tempTime - tempTime_p

        data.append(str(timeDiff))


    df.loc[line] = data
    line += 1
    run += 1

    df.to_csv(outputName, header = True)
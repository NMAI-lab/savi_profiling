'''
    Parsing from XML into CSV
'''

import os
import pandas as pd
from lxml import etree

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def profileXmlToCsv(inputDir):
    
    interestedFunctions = ['reasoningCycle',
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
                           'deliberate',
                           'sense',
                           'act']

    outputPath = inputDir + 'Cumulative_Data/'
    outputName = outputPath + 'Cumulative.csv'
    if (not os.path.exists(outputPath)):
        os.mkdir(outputPath)
    if os.path.exists(outputName):
        os.remove(outputName)

    # Get the names of all the XML files
    xmlFiles = list()
    for file in os.listdir(inputDir):
        if file.endswith(".xml"):
            xmlFiles.append(file)

    line = 1
    df = pd.DataFrame(columns = interestedFunctions)

    for file in xmlFiles:
        printProgressBar (line, len(xmlFiles))
        runFile = inputDir + file
        p = etree.XMLParser(huge_tree = True)
        doc = etree.parse(runFile, parser = p)
    
        row = []    
        for functionName in interestedFunctions:
            functionData = doc.find(".//node[@methodName='" + functionName + "']")
            if functionData == None:
                row.append('-1')
            else:
                row.append(str(functionData.get("time")))
         
        df.loc[line] = row
        line += 1
        
    
    df.to_csv(outputName, header = True)
    
    
def analyze():
    directoryList = ["Y:/School/PhD/ProfileResults/car/deliberate/profiles/",
                     "Y:/School/PhD/ProfileResults/car/reassoningCycle/profiles/",
                     "Y:/School/PhD/ProfileResults/gridRosPC/decide/profiles/",
                     "Y:/School/PhD/ProfileResults/gridRosPC/reasoningCycle/profiles/",
                     "Y:/School/PhD/ProfileResults/gridSynched/reasoningCycle/profiles/",
                     "Y:/School/PhD/ProfileResults/gridSynched/synchGridDeliberate/profiles/",
                     "Y:/School/PhD/ProfileResults/mail/deliberate/profiles/",
                     "Y:/School/PhD/ProfileResults/mail/reasoningCycle/profiles/",
                     "Y:/School/PhD/ProfileResults/rosGridRpi/deliberate/profiles/",
                     "Y:/School/PhD/ProfileResults/rosGridRpi/reasoningCycle/profiles/"]
    
    for i in range(len(directoryList)):
        print("Convertig " + str(i) + " of " + str(len(directoryList)))
        profileXmlToCsv(directoryList[i])
    print("Done")
    
    
    
if __name__ == '__main__':
    analyze()
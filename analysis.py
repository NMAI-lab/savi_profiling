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
                           'deliberate']

    outputPath = inputDir + '/Cumulative_Data'
    outputName = outputPath + '/Cumulative.csv'
    if (not os.path.exists(outputPath)):
        os.mkdir(outputPath)

    xmlFiles = list()
    for file in os.listdir(inputDir):
        if file.endswith(".xml"):
            xmlFiles.append(file)

    line = 1
    df = pd.DataFrame(columns = interestedFunctions)
    
    run = 1
    while (True):
        printProgressBar (run, len(xmlFiles))
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
        
        deliberateNode_p = doc_p.find("//node[@methodName=\"deliberate\"]")
        deliberateNode = doc.find("//node[@methodName=\"deliberate\"]")
        
        if ((rcNode_p == None) and (rcNode == None)):
            if ((deliberateNode_p == None) and (deliberateNode == None)):
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
    
    
def analyze():
    directoryList = ["Y:/School/PhD/ProfileResults/car/deliberate/profiles",
                     "Y:/School/PhD/ProfileResults/car/reassoningCycle/profiles",
                     "Y:/School/PhD/ProfileResults/gridRosPC/decide/profiles",
                     "Y:/School/PhD/ProfileResults/gridRosPC/reasoningCycle/profiles",
                     "Y:/School/PhD/ProfileResults/gridSynched/reasoningCycle/profiles",
                     "Y:/School/PhD/ProfileResults/gridSynched/synchGridDeliberate/profiles",
                     "Y:/School/PhD/ProfileResults/mail/deliberate/profiles",
                     "Y:/School/PhD/ProfileResults/mail/reasoningCycle/profiles",
                     "Y:/School/PhD/ProfileResults/rosGridRpi/deliberate/profiles",
                     "Y:/School/PhD/ProfileResults/rosGridRpi/reasoningCycle/profiles"]
  
    for i in range(len(directoryList)):
        print("Convertig " + str(i) + " of " + str(len(directoryList)))
        profileXmlToCsv(directoryList[i])
    print("Done")
    
    
    
if __name__ == '__main__':
    analyze()
import csv
import pandas as pd

pullData =[]
with open('SheetPullData.csv', newline='') as csvfile:
    pulls = csv.reader(csvfile, delimiter=',')
    for row in pulls:
        pullData.append(row)
pullData = pd.DataFrame(pullData, columns = pullData[0])
print(pullData.columns)
AData = pullData.loc[pullData["HH_ID"] == "A"]
BData = pullData.loc[pullData["HH_ID"] == "B"]
CData = pullData.loc[pullData["HH_ID"] == "C"]
DData = pullData.loc[pullData["HH_ID"] == "D"]
print(AData)
combinedData = []
taskTime = 30
sheetCounter = 0
numPulls = 0
#AData.sort_values(by = ["Time Rank"])
for a in AData.itertuples():
    print(a[6])
    if int(a[6]) > taskTime:
        combinedData.append([a[1], a[2], a[3], a[4], a[5],a[6],sheetCounter, numPulls, a[8]])
        numPulls = 1
        sheetCounter = float(a[7])
    elif int(a[6]) <= taskTime:
        sheetCounter += float(a[7])
        numPulls +=1
    else:
        pass
sheetCounter = 0
numPulls = 0
#BData.sort_values(by = ["Time Rank"])
for b in BData.itertuples():
    #print(b[6])
    if int(b[6]) > taskTime:
        combinedData.append([b[1], b[2], b[3], b[4], b[5],b[6],sheetCounter, numPulls, b[8]])
        numPulls = 1
        sheetCounter = float(b[7])
    elif int(b[6]) <= taskTime:
        sheetCounter += float(b[7])
        numPulls +=1
    else:
        pass
sheetCounter = 0
numPulls = 0
#CData.sort_values(by = ["Time Rank"])
for c in CData.itertuples():
    if int(c[6]) > taskTime:
        combinedData.append([c[1], c[2], c[3], c[4], c[5], c[6],sheetCounter, numPulls, c[8]])
        numPulls = 1
        sheetCounter = float(c[7])
    elif int(c[6]) <= taskTime:
        sheetCounter += float(c[7])
        numPulls +=1
    else:
        pass
sheetCounter = 0
numPulls = 0
#DData.sort_values(by = ["Time Rank"])
for d in DData.itertuples():
    if int(d[6]) > taskTime:
        combinedData.append([d[1], d[2], d[3], d[4], d[5],d[6],sheetCounter, numPulls,d[8]])
        numPulls = 1
        sheetCounter = float(d[7])
    elif int(d[6]) <= taskTime:
        sheetCounter += float(d[7])
        numPulls +=1
    else:
        pass

combinedData = pd.DataFrame(combinedData, columns = ["2","HH_ID", "Roll_ID", "Roll_Type", "Timestamp", "TimeSinceLastPull", "Total Sheets", "Number of Pulls", "Time Rank"])
#combinedData.sort_values(by = ["Time Rank"], ascending = False)
#combinedData.drop("1")
#combinedData.drop("2")
combinedData.to_csv("Data.csv", header = True)


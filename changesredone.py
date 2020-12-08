import csv
import random as rd
import time
import pandas as pd
import os
import re


#Uploading file
try:
    read_file = pd.read_excel (r'changes.xls')
    read_file.to_csv (r'changes.csv', index = None, header=True)
except:
    try:
        read_file = pd.read_excel (r'changes.xlsx')
        read_file.to_csv (r'changes.csv', index = None, header=True)
    except:
        print("file not found")


start_time = time.time()

ctnr_name_pattern = re.compile(4*"\w"+7*"\d")
ctnr_location_pattern = re.compile(6*"\d")

#parsing content

with open('changes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0

    cntnr = []
    fr = []
    to = []

    for row in csv_reader :
        for i in range(len(row)):
            match_ctnr= re.search(ctnr_name_pattern, row[i])
            match_loc_fr = re.search(ctnr_location_pattern, row[i])

            if match_ctnr:
                cntnr.append(match_ctnr.group())
            elif match_loc_fr:
                for j in range(i+1,len(row)):
                    match_loc_to = re.search(ctnr_location_pattern, row[j])
                    if match_loc_to:
                        fr.append(match_loc_fr.group())
                        to.append(match_loc_to.group())
                        break

resultcntnr = []
sortedfr = []
resultto = []
resultfr = []

#sorting function

flag = True

while flag:
    flag = False
    for i in range(len(to)):
        if to[i] not in fr:
            flag = True
            resultcntnr.append(cntnr[i])
            sortedfr.append(fr[i])
            resultfr.append(fr[i])
            resultto.append(to[i])

            cntnr.pop(i)
            fr.pop(i)
            to.pop(i)
            break

sortedto = []
sortedcntrn = []
sortedfr.sort(reverse = True)


for i in range(len(sortedfr)):
    sortedto.append(resultto[resultfr.index(sortedfr[i])])
    sortedcntrn.append(resultcntnr[resultfr.index(sortedfr[i])])

print("----------------------------------------------")
print("Chained changes")
print("----------------------------------------------")

for i in range(len(resultcntnr)):
    print(str(sortedcntrn[i])+" - From : "+str(sortedfr[i])+" - To : "+str(sortedto[i]))


resultCntnr = []
resultFr = []
resultTo = []

checkList = [x for x in range(len(cntnr))]

while checkList:
    i = rd.choice(checkList)
    checkList.remove(i)
    check = fr[i]
    resultCntnr.append(cntnr[i])
    resultFr.append(fr[i])
    resultTo.append(to[i])
    while True:
        i = fr.index(to[i])
        resultCntnr.append(cntnr[i])
        resultFr.append(fr[i])
        resultTo.append(to[i])
        checkList.remove(i)
        if to[i] == check:
            resultCntnr.append("-------------------")
            resultFr.append(' ')
            resultTo.append(' ')
            break

#output


print("----------------------------------------------")
print("Linked Changes")
print("----------------------------------------------")

for i in range(len(resultCntnr)):
    if resultCntnr[i] != "-------------------":
        print(str(resultCntnr[i])+" - From : "+str(resultFr[i])+" - To : "+str(resultTo[i]))
    else:
        print(str(resultCntnr[i]))


os.remove("changes.csv")

print("--- %s seconds to run ---" % (time.time() - start_time))
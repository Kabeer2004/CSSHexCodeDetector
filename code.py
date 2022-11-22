# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
cssCode = []
for i in range (0,n):
    cssCode.append(input())
opencurly = []
closedcurly = []
for i in range(len(cssCode)):
    if cssCode[i] == "{" or cssCode[i].find("{")!=-1:
        opencurly.append(i)
    elif cssCode[i] == "}"or cssCode[i].find("}")!=-1:
        closedcurly.append(i)
interestedArea = []
#print (opencurly)
#print (closedcurly)
for i in range(0,len(opencurly)):
    start=opencurly[i]
    end = closedcurly[i]
    currentSlice = cssCode[start+1:end]
    interestedArea.append(currentSlice)
hashList = []
for i in range (0,len(interestedArea)):
    for j in range (len(interestedArea[i])):
        temp = interestedArea[i][j].split()
        for t in temp:
            if t.startswith('#') :
                try:
                    t = t.replace(';','')
                except:
                    pass
                finally:
                    pass
                try: 
                    t = t.replace(',','')
                except:
                    pass
                finally:
                    pass
                try:
                    t = t.replace(')','')
                except:
                    pass
                finally:
                    pass
                hashList.append(t)
            elif t.find("#")!=-1:
                x = t.find("#")
                t = t[x:]
                try:
                    t = t.replace(';','')
                except:
                    pass
                finally:
                    pass
                try: 
                    t = t.replace(',','')
                except:
                    pass
                finally:
                    pass
                try:
                    t = t.replace(')','')
                except:
                    pass
                finally:
                    pass
                hashList.append(t)
finalList = [] 
checkList = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','a','b','c','d','e','f','#']
for a in hashList:
    valid = True
    for i in range(len(a)):
        if a[i] not in checkList:
            valid = False
            break
        else:
            continue
    if valid:
        finalList.append(a)

for i in range(len(finalList)):
    print (finalList[i])

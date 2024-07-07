

def lengthOfLongestSubstring(s):
    startPoint = 0
    endPoint = 0
    convList = list(s)
    checkSet = set()
    baseString = ''
    substringList = []
    while endPoint != len(convList):
        if convList[endPoint] not in checkSet:
            baseString = baseString + convList[endPoint]
            checkSet.add(convList[endPoint])
            endPoint = endPoint+1
        else:
            substringList.append(len(baseString))
            baseString = ''
            checkSet.clear()
            endPoint = startPoint = startPoint+1
    substringList.append(len(baseString))
    if len(substringList) != 0:
        return max(substringList)
    else:
        return 0

s = " "
print(lengthOfLongestSubstring(s))
        


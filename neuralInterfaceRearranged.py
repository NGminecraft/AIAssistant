 def saving(keywords, values):
    print("Saving")
    import json
    d = open('weights.json', 'w')
    values = values + keywords
    json.dump(values, d)
    print("Done")


def didntWork(output, query, keywords):
    # Scanning through the query list and keywords to find what ran
    queryList = str.split(query)
    test = 0
    keywordsDraft = [""]
    keywordsUsed = [""]
    multipleKeywords = 0
    if n < len(queryList):
        for n in queryList:
            if n in keywords:
                keywordsDraft = keywordsDraft.append(str(n))
                if keywordsDraft != None:
                    keywordsUsed.append(queryList)
            n += 1
    else:
        print("That may be because we didn't detect any keywords.")
    # increase weight value by 0.1
    values = loader()
    for multipleKeywords in keywordsUsed:
        for i in values:
            valuesGreatestLocation = int(values[0][i].index(max(values[0][i])))
            test = valuesGreatestLocation
            for k in queryList:
                if k in keywords:
                    keywordLocation = keywords.index(k)
                    if test == keywordLocation:
                        i[test] += 0.1
            i += 1
        multipleKeywords += 1
    saving(keywords, values)


def worked(query, keywords):
    # Looking for unknown keywords
    queryList = str.split(query)
    counter = 0
    for counter in queryList:
        if counter in keywords:
            counter += 1
        else:
            if counter.isnumeric() == True:
                counter += 1
            else:
                if counter.capitalize() in keywords:
                    counter += 1
                else:
                    keywords.append(str(counter))
                    counter += 1
    saving(keywords, loader())


def feedback(output, query, keywords):
    feedbackRecieved = input("Did it run right? y/n. ")
    if feedbackRecieved == "y":
        worked(query, keywords)
    elif feedbackRecieved == "n":
        didntWork(output, query, keywords)
    else:
        pass
    

def output1():
    import time
    if int(time.strftime("%H", time.localtime())) - 6 > 12:
        hours = (int(time.strftime("%H", time.localtime())) - 6) - 12
        halfDay = "PM"
    else:
        hours = int(time.strftime("%H", time.localtime())) - 6
        halfDay = "AM"
        if hours == 12:
            halfDay = "PM"
    
    print("The time is", hours, ":", time.strftime("%M", time.localtime()), halfDay, "with", time.strftime("%S", time.localtime()), "seconds.")


def output2():
    import time
    from datetime import date
    if int(time.strftime("%H", time.localtime())) - 6 > 12:
        hours = (int(time.strftime("%H", time.localtime())) - 6) - 12
        halfDay = "PM"
    else:
        hours = int(time.strftime("%H", time.localtime())) - 6
        halfDay = "AM"
        if hours == 12:
            halfDay = "PM"
    
    print("The day today is", date.today(), "and the time is", hours, ":", time.strftime("%M", time.localtime()), halfDay, "with", time.strftime("%S", time.localtime()), "seconds.")


def output3():
    from datetime import date
    print("Today is ", date.today(), ".")


def mathSolver(first, operator, second):
    solution = 0
    if operator == "Multiplication":
        solution = first * second
    if operator == "Division":
        solution = first / second
    if operator == "Addition":
        solution = first + second
    if operator == "Subtraction":
        solution = first - second
    try:
        int(solution)
    except:
        print("The answer is", solution)  
    else:
        print("The answer is", int(solution))



def output4(query, parenthasesOpen = None, parenthasesClose = None):
    if parenthasesOpen != None:
        containsMath = query.split[parenthasesOpen + 1]
    containsMath = query.split()
    location = 0
    numberBefore = 0
    numberAfter = 0
    operator = ""
    parenthases = False
    if "*" in containsMath:
        location = containsMath.index("*")
        operator = "Multiplication"
    if "-" in containsMath:
        location = containsMath.index("-")
        operator = "Subtraction"
    if "+" in containsMath:
        location = containsMath.index("+")
        operator = "Addition"
    if "/" in containsMath:
        location = containsMath.index("/")
        operator = "Division"
    if containsMath[location + 1].isnumeric():
        numberAfter = float(containsMath[location + 1])
    if containsMath[location - 1].isnumeric():
        numberBefore = float(containsMath[location - 1])
    if "(" in containsMath:
        openParenthases = containsMath.index("(")
        try:
            closeParenthases = containsMath.index(")")
        except:
            print("Please add closing parenthases")
        else:
            closeParenthases = containsMath.index(")")
            parenthases = True
    if parenthases == True:
        output4(openParenthases, closeParenthases)
    mathSolver(numberBefore, operator, numberAfter)


def executer(values, query):
    output=values.index(max(values))
    if output == 0:
        output1()
    elif output == 1:
        output2()
    elif output == 2:
        output3()
    elif output == 3:
        output4(query)
    return


def ReLU(x):
    return max(0, (x))


def weight1Values(keywords, y, x, counter = 0, result = 0):
    while counter < keywords:
        result += y[counter] * x[counter]
        counter += 1
    else:
        return result


def brains(keywords, inputVector, weight1_1Values, weight1_2Values, weight1_3Values, weight1_4Values, weight1_5Values, weight2_1Values, weight2_2Values, weight2_3Values, weight2_4Values, weight3_1Values, weight3_2Values, weight3_3Values, weight3_4Values):
    # A big mess of refrencing, it gets the job done though
    dotPoint1_1 = ReLU(weight1Values(keywords, inputVector, weight1_1Values))
    dotPoint1_2 = ReLU(inputVector[0] * weight1_2Values[0] + inputVector[1] * weight1_2Values[1] + weight1_2Values[2] * weight1_2Values[2] + inputVector[3] * weight1_2Values[3] + inputVector[4] * weight1_2Values[4] + inputVector[5] * weight1_2Values[5] + inputVector[6] * weight1_2Values[6])
    dotPoint1_3 = ReLU(inputVector[0] * weight1_3Values[0] + inputVector[1] * weight1_3Values[1] + inputVector[2] * weight1_3Values[2] + inputVector[3] * weight1_3Values[3] + inputVector[4] * weight1_3Values[4] + inputVector[5] * weight1_3Values[5] + inputVector[6] * weight1_3Values[6])
    dotPoint1_4 = ReLU(inputVector[0] * weight1_4Values[0] + inputVector[1] * weight1_4Values[1] + inputVector[2] * weight1_4Values[2] + inputVector[3] * weight1_4Values[3] + inputVector[4] * weight1_4Values[4] + inputVector[5] * weight1_4Values[5] + inputVector[6] * weight1_4Values[6])
    dotPoint2_1 = ReLU(dotPoint1_1 *  weight2_1Values[0] + dotPoint1_2 * weight2_1Values[1] + dotPoint1_3 * weight2_1Values[2] + dotPoint1_4 * weight2_1Values[3])
    dotPoint2_2 = ReLU(dotPoint1_1 * weight2_2Values[0] + dotPoint1_2 * weight2_2Values[1] + dotPoint1_3 * weight2_2Values[2] + dotPoint1_4 * weight2_2Values[3])
    dotPoint2_3 = ReLU(dotPoint1_1 * weight2_3Values[0] + dotPoint1_2 * weight2_3Values[1] + dotPoint1_3 * weight2_3Values[2] + dotPoint1_4 * weight2_3Values[3])
    dotPoint2_4 = ReLU(dotPoint1_1 * weight2_4Values[0] + dotPoint1_1 * weight2_4Values[1] + dotPoint1_3 * weight2_4Values[2] + dotPoint1_4 * weight2_4Values[3])
    outputDot1 = ReLU(dotPoint2_1 * weight3_1Values[0] + dotPoint2_2 * weight3_1Values[1] + dotPoint2_3 * weight3_1Values[2] + dotPoint2_4 * weight3_1Values[3])
    outputDot2 = ReLU(dotPoint2_1 * weight3_1Values[0] + dotPoint2_2 * 1.5 + dotPoint2_3 * -1 + dotPoint2_4 * 0)
    outputDot3 = ReLU(dotPoint2_1 * 1.5 + dotPoint2_2 * -1 + dotPoint2_3 * -1 + dotPoint2_4 * 0)
    outputDot4 = ReLU(dotPoint2_1 * 0 + dotPoint2_2 * 0 + dotPoint2_3 * 0 + dotPoint2_4 * 1.2)
    return [outputDot1, outputDot2, outputDot3, outputDot4]


def loader(i):
    import json
    with open('weights.json') as p:
        while True:
            try:
                data = list(json.load(p))
                if i == "keywords":
                    return data[-1]
                else:
                    return data[i]
            except:
                raise


def vectorCreator(keywords, query):
    # Generating an upper and lowercase keyword list
    keywordLower = []
    keywordUpper = []
    for keywordCounter in keywords :
        keywordLower.append(str.lower(keywordCounter))
        keywordUpper.append(str.upper(keywordCounter))
    # prepping the variables
    vectorCounter = 0    
    vectorRoughDraft = []
    inputVector = [0,0,0,0,0,0]
    queryList = query.split()
    # Building the vector
    for vectorCounter in keywords:
        if  queryList.count(keywords[vectorCounter]) > 0:
            vectorRoughDraft.append(1)
        elif queryList.count(keywordUpper[vectorCounter]) > 0:
            vectorRoughDraft.append(1)
        elif queryList.count(keywordLower[vectorCounter]) > 0:
            vectorRoughDraft.append(1)
        else:
            vectorRoughDraft.append(0)
    else:
        inputVector = vectorRoughDraft
        return inputVector


def weightLoader(i):
    values = list("")
    counter = 0
    for i in loader(i):
        print(i)
        spacer = values.append(loader(counter))
        try:
            while x < spacer:
                    if spacer[x] == None:
                        spacer = spacer.remove(None)
                        values.append(spacer)
                        return values
                    x += 1
        except:
            return values
        counter += 1


def main():
    # asks for query
    query = input("What do you want this time? ")
    # Generates all the weight values
    weight1Values = weightLoader(0) # Weight 1 Values will stay as a list
#    weight1Values = weightValues[0]
    weight2Values = weightLoader(1)
    print(weight2Values)
#    weight2Values = weightValues[1]
    weight2_1Values = list(weight2Values[0])
    weight2_2Values = list(weight2Values[1])
    weight2_3Values = list(weight2Values[2])
    weight2_4Values = list(weight2Values[3])
    weight3Values = weightLoader[2]
#    weight3Values = weightValues[2]
    weight3_1Values = list(weightValues[9])
    weight3_2Values = list(weightValues[10])
    weight3_3Values = list(weightValues[11])
    weight3_4Values = list(weightValues[12])
    keywords = loader("keywords")
    inputVector = vectorCreator(keywords, query)
    outputList = brains(keywords, inputVector, weight1_1Values, weight1_2Values, weight1_3Values, weight1_4Values, weight1_5Values, weight2_1Values, weight2_2Values, weight2_3Values, weight2_4Values, weight3_1Values, weight3_2Values, weight3_3Values, weight3_4Values)
    executer(outputList, query)
    feedback(outputList, query, keywords)
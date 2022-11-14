def entireJson():
    from json import load
    with open("weights.json", "r") as w:
        return load(w)
    

def saving(keywords, values):
    print("Saving")
    from json import dump
    d = open('weights.json', 'w')
    values.remove(values[-1])
    values.append(keywords)
    dump(values, d)
    print("Done")


def didntWork(output, query, keywords):
    # Scanning through the query list and keywords to find what ran
    queryList = str.split(query)
    keywordsUsed = [""]
    for n in queryList:
        if n in keywords:
            keywordsUsed.append(n)
    
    # increase weight value by 0.1
    
    saving(keywords, entireJson())


def worked(query, keywords):
    # Looking for unknown keywords
    queryList = str.split(query)
    counter = 0
    while counter < len(queryList):
        if queryList[counter] in keywords:
            counter += 1
        else:
            if queryList[counter].isnumeric() == True:
                counter += 1
            else:
                if queryList[counter].capitalize() in keywords:
                    counter += 1
                else:
                    keywords.append(str(queryList[counter].capitalize()))
                    counter += 1
    saving(keywords, entireJson())


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
    output = values.index(max(values))
    if output == 0:
        output1()
    elif output == 1:
        output2()
    elif output == 2:
        output3()
    elif output == 3:
        output4(query)
    feedback = input("Did it work right? y/n ")
    if feedback == "y":
        worked(query, keywordsLoader())
    else:
        didntWork(output, query, keywordsLoader())
    return


def ReLU(x):
    return max(0, x)


def neuron1Creater():
    pass



def weightsCreator(b, a, i):
    # Layer, neuron value, and weight value
    from json import load
    with open("weights.json", "r") as w:
        json = load(w)
    return json[b][a][i]


def neuronSolver(l, a, vector):
    # Takes in a layer, neuron location value and the input vector and returns the value
    value = 0
    i = 0
    while i < len(vector):
        value = value + (weightsCreator(l, a, i) * vector[i])
        i += 1
    return value


def brains(vector):
    # Solving for neurons neuron layer_value
    neuron1_1 = ReLU(neuronSolver(0, 0, vector))
    neuron1_2 = ReLU(neuronSolver(0, 1, vector))
    neuron1_3 = ReLU(neuronSolver(0, 2, vector))
    neuron1_4 = ReLU(neuronSolver(0, 3, vector))
    neuron2_1 = (weightsCreator(1, 0, 0) * neuron1_1) + (weightsCreator(1, 0, 1) * neuron1_2) + (weightsCreator(1, 0, 2) * neuron1_3) + (weightsCreator(1, 0, 3) * neuron1_4)
    neuron2_2 = (weightsCreator(1, 1, 0) * neuron1_1) + (weightsCreator(1, 1, 1) * neuron1_2) + (weightsCreator(1, 1, 2) * neuron1_3) + (weightsCreator(1, 1, 3) * neuron1_4)
    neuron2_3 = (weightsCreator(1, 2, 0) * neuron1_1) + (weightsCreator(1, 2, 1) * neuron1_2) + (weightsCreator(1, 2, 2) * neuron1_3) + (weightsCreator(1, 2, 3) * neuron1_4)
    neuron2_4 = (weightsCreator(1, 3, 0) * neuron1_1) + (weightsCreator(1, 3, 1) * neuron1_2) + (weightsCreator(1, 3, 2) * neuron1_3) + (weightsCreator(1, 3, 3) * neuron1_4)
    neuron3_1 = (weightsCreator(2, 0, 0) * neuron2_1) + (weightsCreator(2, 0, 1) * neuron2_2) + (weightsCreator(2, 0, 2) * neuron2_3) + (weightsCreator(2, 0, 3) * neuron2_4)
    neuron3_2 = (weightsCreator(2, 1, 0) * neuron2_1) + (weightsCreator(2, 1, 1) * neuron2_2) + (weightsCreator(2, 1, 2) * neuron2_3) + (weightsCreator(2, 1, 3) * neuron2_4)
    neuron3_3 = (weightsCreator(2, 2, 0) * neuron2_1) + (weightsCreator(2, 2, 1) * neuron2_2) + (weightsCreator(2, 2, 2) * neuron2_3) + (weightsCreator(2, 2, 3) * neuron2_4)
    neuron3_4 = (weightsCreator(2, 3, 0) * neuron2_1) + (weightsCreator(2, 3, 1) * neuron2_2) + (weightsCreator(2, 3, 2) * neuron2_3) + (weightsCreator(2, 3, 3) * neuron2_4)
    return [neuron3_1, neuron3_2, neuron3_3, neuron3_4]


def keywordsLoader():
    from json import load
    with open("weights.json", "r") as w:
        json = load(w)
    return json[-1]


def vectorCreator(query):
    keywords = keywordsLoader()
    vector = []
    for i in query.split():
        if i in keywords:
            vector.append(1)
        else:
            vector.append(0)
    return vector


def main(query = ""):
    query = input("What would you like to do? ")
    inputVector = vectorCreator(query)
    outputList = brains(inputVector)
    executer(outputList, query)

def saver():
    import json


def finisher():
    feedback = input("On a scale of 0-5 how well did it work? ")
    try:
        int(feedback)
    except:
        print("Please enter an integer.")
        return
    else:
        feedback = int(feedback)
        if feedback != 5:
            feedback2 = input("Did something different run?")
        
    

    
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
    print("Today is the", date.today(), ".")


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
        print("The answ er is", solution)  
    else:
        print("The answer is", int(solution))



def output4(parenthasesOpen, parenthasesClose):
    if parenthasesOpen != None:
        containsMath = inputRecievedList[parenthasesOpen + 1]
    containsMath = inputRecievedList
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


def executer(values):
    output=values.index(max(values))
    if output == 0:
        output1()
    elif output == 1:
        output2()
    elif output == 2:
        output3()
    elif output == 3:
        output4(None, None)
    #finisher()

def ReLU(x):
    return max(0, x)


"""
The weight values are stored in weight.json. The json is a list. The lists inside are the layers, and the lists inside those are the weight values by neuron [weigths[layer[neuron weight values (outgoing)]
"""


def weight(inputVector):
    dotPoint1_1 = ReLU(inputVector[0] * weight1_1Values[0] + inputVector[1] * weight1_1Values[1] + inputVector[2] * weight1_1Values[2] + inputVector[3] * weight1_1Values[3] + inputVector[4] * weight1_1Values[4])
    dotPoint1_2 = ReLU(inputVector[0] * weight1_2Values[0] + inputVector[1] * weight1_2Values[1] + weight1_2Values[2] * weight1_2Values[2] + inputVector[3] * weight1_2Values[3] + inputVector[4] * weight1_2Values[4])
    dotPoint1_3 = ReLU(inputVector[0] * 2.5 + inputVector[1] * 0 + inputVector[2] * 0 + inputVector[3] * 0 + inputVector[4] * 0.5)
    dotPoint1_4 = ReLU(inputVector[0] * 0.1 + inputVector[1] * 0 + inputVector[2] * 0.1 + inputVector[3] * 2 + inputVector[4] * 1.3)
    dotPoint2_1 = ReLU(dotPoint1_1 *  2 + dotPoint1_2 * -1 + dotPoint1_3 * -1 + dotPoint1_4 * 1.2)
    dotPoint2_2 = ReLU(dotPoint1_1 * 0.3 + dotPoint1_2 * 2 + dotPoint1_3 * 0.4 + dotPoint1_4 * 1.2)
    dotPoint2_3 = ReLU(dotPoint1_1 * -1 + dotPoint1_2 * -1 + dotPoint1_3 * 2 + dotPoint1_4 * 1.2)
    dotPoint2_4 = ReLU(dotPoint1_1 * 0 + dotPoint1_1 * 0 + dotPoint1_3 * 0 + dotPoint1_4 * 1.55)
    outputDot1 = ReLU(dotPoint2_1 * -1 + dotPoint2_2 * -1 + dotPoint2_3 * 1.5 + dotPoint2_4 * 0)
    outputDot2 = ReLU(dotPoint2_1 * -1 + dotPoint2_2 * 1.5 + dotPoint2_3 * -1 + dotPoint2_4 * 0)
    outputDot3 = ReLU(dotPoint2_1 * 1.5 + dotPoint2_2 * -1 + dotPoint2_3 * -1 + dotPoint2_4 * 0)
    outputDot4 = ReLU(dotPoint2_1 * 0 + dotPoint2_2 * 0 + dotPoint2_3 * 0 + dotPoint2_4 * 1.2)
    executer([outputDot1, outputDot2, outputDot3, outputDot4])

def startup(possibleInputs):
    gen = loader()
    weight1Values = list(next(loader()))
    # getting the values of all the weight so they can be refrenced easier above
    global weight1_1Values
    global weight1_2Values
    global weight1_3Values
    global weight1_4Values
    global weight1_5Values

    global weight2_1Values
    global weight2_2Values
    global weight2_3Values
    global weight2_4Values

    global weight3_1Values
    global weight3_2Values
    global weight3_3Values
    global weight3_4Values
    weight1_1Values = list(weight1Values[0])
    weight1_2Values = list(weight1Values[1])
    weight1_3Values = list(weight1Values[2])
    weight1_4Values = list(weight1Values[3])
    weight1_5Values = list(weight1Values[-1])
    weight2Values = list(next(loader()))
    wieght2_1Values = list(weight2Values[0])
    wieght2_2Values = list(weight2Values[1])
    wieght2_3Values = list(weight2Values[2])
    wieght2_4Values = list(weight2Values[3])
    weight3Values = list(next(loader()))
    weight3_1Values = list(weight3Values[0])
    weight3_2Values = list(weight3Values[1])
    weight3_3Values = list(weight3Values[2])
    weight3_4Values = list(weight3Values[3])
    global keywords
    keywords = list(possibleInputs)
    print(keywords)
    global inputRecieved
    inputRecieved = input("Whats up? ")
    """    if "time" in inputRecieved or "Time" in inputRecieved:
        inputVector[0] = 1
    if "Day" in inputRecieved or "day" in inputRecieved or "Date" in inputRecieved or 'date' in inputRecieved:
        inputVector[1] = 1
    if "and" in inputRecieved or "And" in inputRecieved:
        inputVector[2] = 1
    if "math" in inputRecieved or "Math" in inputRecieved or "solve" in inputRecieved or "Solve" in inputRecieved:
        inputVector[3] = 1
    if "What" in inputRecieved or "what" in inputRecieved or "What's" in inputRecieved or "what's" in inputRecieved or "Whats" in inputRecieved or "whats" in inputRecieved:
        inputVector[4] = 1
    weight(inputVector)"""
    vectorCreatorClass.setup(keywords)


class vectorCreatorClass():    
    """def creator(vectorBuilder, keywords, possibleInputs):
        vectorCreator = 0
        inputVectorBuilder = 0
        vectorCounter = 0
        inputVector = [0]
        inputStr = str.split(inputRecieved)
        keywordRemoved = ""
        vectorCounter = 0
        inputVector = [0] * 5
        while vectorCreator < len(keywords):
            print(vectorCreator)
            while str(possibleInputs[vectorCreator]) in inputRecieved:
                keywordRemoved = str(possibleInputs[vectorCreator])
                vectorBuilder[vectorCreator] = 1
                inputStr = inputStr.remove(keywordRemoved)
                if 1 in vectorBuilder[vectorCounter:vectorCounter + 1]:
                    inputVector.append(1)
                    inputVectorBuilder += 1
                    vectorCounter += 2
                else:
                    print(inputVector)
                    inputVector.append(0)
                    vectorCounter += 2
                vectorCreator += 1
            else:
                vectorCreator += 1
        else:
            print(vectorCreator)
            print(inputVector)
            weight(inputVector)"""
    def creatorTest(keywords, vectorCreator, inputVectorBuilder, inputVector, inputStr, keywordRemoved, vectorCounter, vectorBuilder):
        while vectorCounter < len(keywords):
            print(inputVector)
            try:
                keywords[vectorCreator]
            except IndexError:
                print(vectorCreator)
                weight(inputVector)
                vectorCreator = 0
            if str(keywords[vectorCreator]) in inputRecieved:
                print("Hi")
                inputStr = str.split(inputRecieved)
                keywordRemoved = str(keywords[vectorCreator])
                vectorBuilder[vectorCreator] = 1
                inputStr = inputStr.remove(keywordRemoved)
                print(vectorCreator)
                print("while")
                print(inputVector)
                vectorCreator += 1
                if 1 in vectorBuilder[vectorCounter:vectorCounter + 1]:
                    inputVector.append(1)
                    print("build")
                    inputVectorBuilder += 1
                    vectorCounter += 2
                else:
                    print(inputVector)
                    print("not build")
                    inputVector.append(0)
                    vectorCounter += 2
                    if vectorCreator == len(keywords) or vectorCreator == -1:
                        print("going")
                        weight(inputVector)
                    else:
                        return
            else:
                vectorCreator += 1
                if vectorCreator == len(keywords) or vectorCreator == -1:
                    print("splat")
                    vectorCretor = 0
                    weight(inputVector)
                elif vectorCreator == len(keywords) - 1:
                    vectorCreator = -1
                else:
                    vectorCreator += 1
        vectorCreator += 1
            
            
    
    
    def setup(keywords):
        print(keywords)
        builder = 0
        listOf0s = [0]
        while builder < len(keywords):
            listOf0s.append(0)
            builder += 1
        vectorCreator = 0
        inputVectorBuilder = 0
        vectorCounter = 0
        inputVector = [0]
        inputStr = str.split(inputRecieved)
        keywordRemoved = ""
        vectorCounter = 0
        inputVector = [0] * 5
        keywords = keywords
        print(keywords)
        vectorCreatorClass.creatorTest(keywords, vectorCreator, inputVectorBuilder, inputVector, inputStr, keywordRemoved, vectorCounter, listOf0s)

def loader():
    import pickle
    with open('data.pickle', "rb") as p:
        while True:
            try:
                yield pickle.load(p)
            except EOFError:
                startup()
    startup()


def main():
    loader()
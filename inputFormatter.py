def ReLU(x):
    return max(0, x)


def brains():
    neuron1 = 


def keywordsLoader():
    from json import loads
    with open("weights.json" "r") as w:
        json = loads(w)
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


def main():
    query = input("What would you like to do?")
    inputVector = vectorCreator(query)
    outputList = brains(inputVector)
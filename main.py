"""
What I want to hopefully become an AI assistant
https://realpython.com/python-ai-neural-network/
https://youtu.be/IQ7sK6PezJo?t=68
"""

"""
Input vector is list of all inputs
weights are the factors

Dot Product = (Input vector 1 * weight vector 1) + (Input vector 2 * input vector 2)
"""
"""
import json
import neuralInterface"""
import inputFormatter
import audioInput
"""
# data = [[[0, 2, 0, 0, 0.5], [0, 0, 2.5, 0, 0.5], [2.5, 0, 0, 0, 0.5], [0.1, 0, 0.1, 2, 1.3]], [[2, -1, -1, 1.2], [0.3, 2, 0.4, 1.2], [-1, -1, 2, 1.2], [0, 0, 0, 1.55]], [[-1, -1, 0.5, 0], [-1, 1.5, -1, 0], [1.5, -1, -1, 0], [0, 0, 0, 1.2]]]

layer1Weights = [[0, 2, 2, 0, 0, 0, 0.5], [0, 0, 0, 2.5, 0, 0, 0.5], [2.5, 0, 0, 0, 0, 0, 0.5], [0.1, 0, 0, 0.1, 2, 2, 1.3]]
layer2Weights = [[2, -1, -1, 1.2], [0.3, 2, 0.4, 1.2], [-1, -1, 2, 1.2], [0, 0, 0, 1.55]]
layer3Weights = [[-1, -1, 0.5, 0], [-1, 1.5, -1, 0], [1.5, -1, -1, 0], [0, 0, 0, 1.2]]
possibleInputs = ["Time", "Day", "Date", "and", "Math", "Solve", "What"]

with open('weights.json') as w:
    data = json.load(w)


def storer():
    d = open('weights.json', 'w')
    values = layer1Weights + layer2Weights + layer3Weights + possibleInputs
    json.dump(values, d)
storer()"""
audioInput.main()
inputFormatter.main()

#how did you figure all og this out? (i'm guessing its google) - ben
# some of it. A lot was just finding ways to put things together - Nick
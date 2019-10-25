import smtplib, random, time, sys

res = ''
values = []

def initVariables():
    corrAns = ""
    substrArr = []
    length = 0
    
    for paramIndex in range(0, len(sys.argv)):
        if (paramIndex == 1):
            corrAns = str(sys.argv[paramIndex])
        elif (paramIndex == 2):
            substrArr = list(sys.argv[paramIndex].split(";"))
        elif (paramIndex == 3):
            length = int(sys.argv[paramIndex])
    
    return (corrAns, substrArr, length)
        

class Selector:
    def __init__(self, correctAnswer, substrArray, length):
        self.CORRECT_ANSWER = correctAnswer
        self.substrArr = substrArray
        self.length = length

        self._values = []
        self._time = 0
    
    def Select(self):
        fullLength = self.length
        substrArr = self.substrArr

        length = fullLength

        nowRes = []
        
        countIndexes = random.randint(1, len(substrArr))
        length -= countIndexes

        for i in range(0, fullLength):
            nowRes.append(" ")
        
        for i in range(0, length):
            randIndex = random.randint(1, fullLength)
            
            while (nowRes[randIndex - 1] != " "):
                randIndex = random.randint(0, length)

            nowRes[randIndex - 1] = str(random.randint(0, 9))
            
        for i in range(0, len(nowRes)):
            if (nowRes[i] == " "):
                toAdd = random.choice(substrArr)
                while toAdd in nowRes:
                    toAdd = random.choice(substrArr)
                nowRes[i] = toAdd
        res = "".join(nowRes)

        if (res in self._values):
            return -1

        self._values.append(res)

        print(res)

        return res
    
    def Check(self):
        return self.Select() == self.CORRECT_ANSWER

    def Run(self):
        _startTime = time.time()

        result = self.Check()

        while not result:
            result = self.Check()

        self._time = time.time() - _startTime

        print("Done. It took " + str(self._time) + " seconds.")

_inputData = initVariables()

CORRECT_ANSWER = _inputData[0]

passwordSelector = Selector(CORRECT_ANSWER, _inputData[1], _inputData[2])

passwordSelector.Run()

input()
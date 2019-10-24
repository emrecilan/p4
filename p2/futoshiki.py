from constraint import *

valueTxt = open("futoshiki_input.txt", "r")
valueList = []
for i in valueTxt:
    valueList.append(i.strip().split(", "))

futoshiki_problem = Problem()

futoshiki_problem.addVariables(["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4","C1", "C2", "C3", "C4", "D1", "D2" ,"D3", "D4"], [1, 2, 3, 4])

futoshiki_problem.addConstraint(AllDifferentConstraint(), ["A1", "A2", "A3", "A4"])
futoshiki_problem.addConstraint(AllDifferentConstraint(), ["B1", "B2", "B3", "B4"])
futoshiki_problem.addConstraint(AllDifferentConstraint(), ["C1", "C2", "C3", "C4"])
futoshiki_problem.addConstraint(AllDifferentConstraint(), ["D1", "D2" ,"D3", "D4"])
futoshiki_problem.addConstraint(AllDifferentConstraint(), ["A1", "B1" ,"C1", "D1"])
futoshiki_problem.addConstraint(AllDifferentConstraint(), ["A2", "B2" ,"C2", "D2"])
futoshiki_problem.addConstraint(AllDifferentConstraint(), ["A3", "B3" ,"C3", "D3"])
futoshiki_problem.addConstraint(AllDifferentConstraint(), ["A4", "B4" ,"C4", "D4"])


for j in valueList:
    a = j[0]
    b = j[1]
    if b.startswith(("1", "2", "3", "4")):
        b = int(b)
        futoshiki_problem.addConstraint(ExactSumConstraint(b), [a])
    else:
        futoshiki_problem.addConstraint(lambda a, b : a > b, [a, b])

solutionSet = futoshiki_problem.getSolutions()[0]

output = str(solutionSet["A1"]) + ", " + str(solutionSet["A2"]) + ", " + str(solutionSet["A3"]) + ", " + str(solutionSet["A4"]) + "\n" + \
         str(solutionSet["B1"]) + ", " + str(solutionSet["B2"]) + ", " + str(solutionSet["B3"]) + ", " + str(solutionSet["B4"]) + "\n" + \
         str(solutionSet["C1"]) + ", " + str(solutionSet["C2"]) + ", " + str(solutionSet["C3"]) + ", " + str(solutionSet["C4"]) + "\n" + \
         str(solutionSet["D1"]) + ", " + str(solutionSet["D2"]) + ", " + str(solutionSet["D3"]) + ", " + str(solutionSet["D4"])

futoshiki_output = open("futoshiki_output.txt", "w")
futoshiki_output.write(output)
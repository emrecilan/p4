from constraint import *

valueTxt = open("kakuro_input.txt", "r")
ListValue = list(valueTxt)
row_value =  []
column_value= []
temp1 = ListValue[0].split(",")
temp2 = ListValue[1].split(",")
for i in temp1:
    row_value.append(i.strip())
for j in temp2:
    column_value.append(j.strip())

row_value1, row_value2, row_value3 = int(row_value[0]), int(row_value[1]), int(row_value[2])
column_value1, column_value2, column_value3 = int(column_value[0]), int(column_value[1]), int(column_value[2])


kakuroa_problem = Problem()

kakuroa_problem.addVariables(["x1", "x2", "x3", "y1", "y2", "y3", "z1", "z2", "z3"], [1, 2, 3, 4, 5, 6, 7, 8, 9])

kakuroa_problem.addConstraint(AllDifferentConstraint(), ["x1", "x2", "x3"])
kakuroa_problem.addConstraint(AllDifferentConstraint(), ["y1", "y2", "y3"])
kakuroa_problem.addConstraint(AllDifferentConstraint(), ["z1", "z2", "z3"])
kakuroa_problem.addConstraint(AllDifferentConstraint(), ["x1", "y1", "z1"])
kakuroa_problem.addConstraint(AllDifferentConstraint(), ["x2", "y2", "z2"])
kakuroa_problem.addConstraint(AllDifferentConstraint(), ["x3", "y3", "z3"])
kakuroa_problem.addConstraint(ExactSumConstraint(column_value1), ["x1", "x2", "x3"])
kakuroa_problem.addConstraint(ExactSumConstraint(column_value2), ["y1", "y2", "y3"])
kakuroa_problem.addConstraint(ExactSumConstraint(column_value3), ["z1", "z2", "z3"])
kakuroa_problem.addConstraint(ExactSumConstraint(row_value1), ["x1", "y1", "z1"])
kakuroa_problem.addConstraint(ExactSumConstraint(row_value2), ["x2", "y2", "z2"])
kakuroa_problem.addConstraint(ExactSumConstraint(row_value3), ["x3", "y3", "z3"])

solutionSet = kakuroa_problem.getSolutions()[0]

output = "x" + ", " + str(row_value1) + ", " + str(row_value2) + ", " + str(row_value3) + "\n" + \
         str(column_value1) + ", " + str(solutionSet["x1"]) + ", " + str(solutionSet["x2"]) + ", " + str(solutionSet["x3"]) + "\n" + \
         str(column_value2) + ", " + str(solutionSet["y1"]) + ", " + str(solutionSet["y2"]) + ", " + str(solutionSet["y3"]) + "\n" + \
         str(column_value3) + ", " + str(solutionSet["z1"]) + ", " + str(solutionSet["z2"]) + ", " + str(solutionSet["z3"])
kakuro_output = open("kakuro_output.txt", "w")
kakuro_output.write(output)




























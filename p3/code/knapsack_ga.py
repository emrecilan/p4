# starter code for solving knapsack problem using genetic algorithm

#   INSTALL NUMPY PACKAGE  BEFORE RUN THE CODE

import random
import numpy

def listToStr(list):
    return ''.join([str(elem) for elem in list])

def strToList(string):
    tempList = []
    for i in string:
        tempList.append(int(i))
    return tempList

def fitnessFunc(population_list): #[chrom,fitnessvalue]
    fitness_list = []
    for i in range(len(population_list)):
        if population_list[i][1][1] > c:
            fitness_list.append([population_list[i][0],0])
        else:
            fitness_list.append([population_list[i][0],population_list[i][1][0]])
    return fitness_list

def get_probability_list(fitness_list): #[chrom,probobality]
    total_fit = 0
    probability_list = []
    for i in range(len(fitness_list)):
        total_fit += fitness_list[i][1]
    if total_fit == 0:
        prob = 1 / len(fitness_list)
        for j in range(len(fitness_list)):
            probability_list.append([fitness_list[j][0],prob])
    else:
        for j in range(len(fitness_list)):
            prob  = (fitness_list[j][1]) / total_fit
            probability_list.append([fitness_list[j][0],prob])
    return probability_list

def tournamentSelection(fitness_list, k):   # [chrom,fitnessvalue]
    parents = []
    while True:
        best = 0
        for i in range(0, k):
            indis = random.randrange(0, len(fitness_list))
            if best == 0 or fitness_list[indis][1] > best:
                best = fitness_list[indis][1]
                bestChrom = population_list[indis]
        if bestChrom not in parents:
            parents.append(bestChrom)
        if len(parents) == 2:
            break
    return parents

def rouletteWheel(probability_list):
    while True:
        chroms = []
        probs = []
        parents = []
        for i in range(len(probability_list)):
            chroms.append(i)
            probs.append(probability_list[i][1])
        choosenIndex = numpy.random.choice(chroms, 2, p=probs)
        parents.append(population_list[choosenIndex[0]])
        parents.append(population_list[choosenIndex[1]])
        if len(parents) == 2:
            break
    return parents

def evaluation(population):
    new_population_list = []
    for i, chrom in enumerate(population):
        vt = 0
        wt = 0
        for j, gene in enumerate(chrom):
            vt += gene * v[j]
            wt += gene * w[j]
        new_population_list.append([chrom, [vt, wt]])
        #[chrom , [value, weight]
    fitnessFunc(new_population_list)
    get_probability_list(fitnessFunc(new_population_list))
    return new_population_list

def evalutionForChrom(chrom):
    new_chrom_list = []
    vt = 0
    wt = 0
    for j, gene in enumerate(chrom):
        vt += gene * v[j]
        wt += gene * w[j]
    new_chrom_list.append([chrom, [vt, wt]])
    # [chrom , [value, weight, fitness, probobality, age]
    return new_chrom_list

def nPointCrossover(n, chrom1, chrom2):
    split_list = []
    lenght = int(len(chrom1))

    while True:
        tempNum = random.randrange(1, lenght)
        if tempNum not in split_list:
            split_list.append(tempNum)
        if len(split_list) == n:
            break
    split_list = sorted(split_list)

    list1 = [chrom1[i: j] for i, j in zip([0] + split_list, split_list + [None])]
    list2 = [chrom2[i: j] for i, j in zip([0] + split_list, split_list + [None])]

    newChrom1 = []
    newChrom2 = []
    index = 0
    while True:
        if index <= n:
            newChrom1 += list1[index]
            newChrom2 += list2[index]
            index += 1
            if index <= n:
                newChrom1 += list2[index]
                newChrom2 += list1[index]
                index += 1
            else:
                break
        else:
            break

    return newChrom1, newChrom2

def mutation(population, mutProb):
    new_population = []
    mutationPoint = random.randrange(0, len(chrom))
    randMutation = random.randrange(0, len(population))
    selectedChrom = population[randMutation]
    if mutProb > 0.5:
        if selectedChrom[mutationPoint] == 1:
            selectedChrom[mutationPoint] = 0
        else:
            selectedChrom[mutationPoint] = 1
    for i in range(len(population_list)):
        ages_list[i][1] += 1
        if population[randMutation] == population_list[i][0]:
            del population_list[i]
            del ages_list[i]
            population_list.insert(i,evalutionForChrom(selectedChrom)[0])
            ages_list.insert(i,[selectedChrom,0])
    for j in range(len(population_list)):
        new_population.append(population_list[j][0])
    return new_population

def sortSecond(val):
    return val[1]

def ageBasedSelect(age_list):
    age_list.sort(key=sortSecond, reverse=True)
    exChrom1 = ages_list[0]
    exChrom2 = ages_list[1]
    return exChrom1,exChrom2

def fitnessBasedSelect(fitness_list):
    fitness_list.sort(key=sortSecond)
    exChrom1 = fitness_list[0]
    exChrom2 = fitness_list[1]

    return exChrom1,exChrom2

def findBest(fitness_list):
    fitness_list.sort(key=sortSecond, reverse = True)
    return fitness_list[0]

def findWorst(fitness_list):
    fitness_list.sort(key=sortSecond)
    return fitness_list[0]
fc = open('./c.txt', 'r')
fw = open('./w.txt', 'r')
fv = open('./v.txt', 'r')
fout = open('./out.txt', 'w')

c = int(fc.readline())
w = []
v = []
for line in fw:
    w.append(int(line))
for line in fv:
    v.append(int(line))

print('Capacity :', c)
print('Weight :', w)
print('Value : ', v)

popSize = int(input('Size of population : '))
genNumber = int(input('Max number of generation : '))
print('\nParent Selection\n---------------------------')
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')
parentSelection = int(input('Which one? '))
if parentSelection == 2:
    k = int(input('k=? (between 1 and ' + str(len(w)) + ') '))
elif 0 > parentSelection or parentSelection > 3:
    print("Invalid Entry")
    print("Enter Valid Entry")
    parentSelection = int(input('Which one? '))

print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))

print('\nMutation Probability\n---------------------------')
mutProb = float(input('prob=? (between 0 and 1) '))

print('\nMutation Probability\n---------------------------')
print('(1) Age-based Selection')
print('(2) Fitness-based Selection')
survivalSelection = int(input('Which one? '))
if 0 > survivalSelection or survivalSelection > 3:
    print("Invalid Entry")
    print("Enter Valid Entry")
    survivalSelection = int(input('Which one? '))
elitism = input('Elitism? (Y or N) ' )
if elitism == "y" or elitism == "Y":
    elitism = True
elif elitism == "n" or elitism == "N":
    elitism = False
else:
    print("Invalid Entry")
    print("Enter Valid Entry")
    elitism = input('Elitism? (Y or N) ')

print('\n----------------------------------------------------------')
print('initalizing population')

population = []
for i in range(popSize):
    temp = []
    for j in range(len(w)):
        temp.append(random.randint(0, 1))
    population.append(temp)

print('evaluating fitnesses')
population_list = []
ages_list =  []
for i, chrom in enumerate(population):
    vt = 0
    wt = 0
    for j, gene in enumerate(chrom):
        vt += gene * v[j]
        wt += gene * w[j]
    #print(i + 1, chrom, vt, wt)
    population_list.append([chrom, [vt, wt]])
    ages_list.append([chrom,0])


##################################################################
genNumber_list = []
valueForGraph = []

bestSolutionList = []
for genvalue in range(genNumber):
    genNumber_list.append(genvalue + 1)
    fitness_list = fitnessFunc(population_list)
    forElitism = findBest(fitness_list)
    evolElitism = evalutionForChrom(forElitism[0])
    if parentSelection == 1:
        fitness_list = fitnessFunc(population_list)
        probability_list = get_probability_list(fitness_list)
        parents = rouletteWheel(probability_list)
    elif parentSelection == 2:
        fitness_list = fitnessFunc(population_list)
        parents = tournamentSelection(fitness_list, k)


    childs = nPointCrossover(n, parents[0][0], parents[1][0])
    childs_list= evaluation(childs)

    mutation(population, mutProb)

    if survivalSelection == 1:
        exChroms = ageBasedSelect(ages_list)
        for indis1 in range(len(population_list)):
            ages_list[i][1] += 1
            if exChroms[0][0] == population_list[indis1][0]:
                del population_list[indis1]
                population_list.insert(indis1, childs_list[0])
                del ages_list[indis1]
                ages_list.insert(indis1, [childs_list[0][0], 0])
            elif exChroms[1][0] == population_list[indis1][0]:
                del population_list[indis1]
                population_list.insert(indis1, childs_list[1])
                del ages_list[indis1]
                ages_list.insert(indis1, [childs_list[1][0], 0])

    elif survivalSelection == 2:
        fitness_list = fitnessFunc(population_list)
        exChroms = fitnessBasedSelect(fitness_list)
        for indis2 in range(len(population_list)):
            ages_list[i][1] += 1
            if exChroms[0][0] == population_list[indis2][0]:
                del population_list[indis2]
                population_list.insert(indis2, childs_list[0])
                del ages_list[indis2]
                ages_list.insert(indis2, [childs_list[0][0], 0])
            elif exChroms[1][0] == population_list[indis2][0]:
                del population_list[indis2]
                population_list.insert(indis2, childs_list[1])
                del ages_list[indis2]
                ages_list.insert(indis2, [childs_list[0][0], 0])
    if elitism:
        worst = findWorst(population_list)
        for index in range (len(population_list)):
            if worst[0][0] == population_list[index][0]:
                del population_list[index]
                population_list.insert(index,evolElitism)

    fitness_list = fitnessFunc(population_list)
    bestSolutionList.append(findBest(fitness_list))
    valueForGraph.append(bestSolutionList[0][1])
#print(findBest(bestSolutionList))
#print(evalutionForChrom(findBest(bestSolutionList)[0]))
solution = evalutionForChrom(findBest(bestSolutionList)[0])
fout.write('chromosome: ' + listToStr(solution[0][0]) + "\n")
fout.write('weight: ' + str(solution[0][1][1]) + "\n")
fout.write('value: ' + str(solution[0][1][0]) + "\n")

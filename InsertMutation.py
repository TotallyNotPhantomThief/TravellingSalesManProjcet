#we basically select randomlyy a gen from chromosome and that get index of it and a index of random target
#after that we swap them in the list without chaning the order of others

import random


def insertMutation(newGen):
 mutatedList = []
 for chromosome in newGen:
  randomGeneToMutate = random.choice(chromosome)
  indexOfGene = chromosome.index(randomGeneToMutate)
  randomTargetPosition =  random.choice(chromosome)
  indexOfTarger = chromosome.index(randomTargetPosition)
  if indexOfGene == indexOfTarger:
   indexOfTarger = chromosome.index(randomTargetPosition)
  placeHolder = randomTargetPosition
  chromosome[indexOfTarger] = randomGeneToMutate
  chromosome[indexOfGene] = placeHolder 
  mutatedList.append(chromosome)
 return mutatedList 
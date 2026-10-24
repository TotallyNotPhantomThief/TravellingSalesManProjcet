#İmported pathlib so ı can read the tsp file from my desktop.
#Tsplib95 lib imported cause its a lib built for tsp problems and helps me load the ids or "genes" in this instance.
#imported math so ı can calculate and compare between diffrend random chromosomes and decide which chromosome is bettere in fitness.

from pathlib import Path
import tsplib95
import random
import math
from RankBasedSelection import rankSolution
from RouletteSelection import rouletteSelection
from NextGeneration import creatingNextGeneration
from InsertMutation import insertMutation
from RandomSlideMutation import randomSlide

file_path = Path.home() / "Desktop" / "kroA100.tsp"

tspFile = tsplib95.load(file_path)

genes = list(tspFile.get_nodes())

def chormosme_creation():
    #Created a copy of the list of id's so the original genepool wont be changed.
    genesCopy = genes.copy()
    random.shuffle(genesCopy)
    return genesCopy

population = []
for i in range(100):
  #adding to the empty population list so we can have a population list duh!!
  population.append(chormosme_creation())

def distanceCalc(city1,city2):
   #eucladian formula cause tsp file is 2d cord system.
   (x1,y1),(x2,y2) = tspFile.node_coords[city1],tspFile.node_coords[city2]
   return math.hypot(x2 - x1, y2 -y1)

def tour_lenght(chromosome):
   total = 0
   for i in range(len(chromosome)):
      city1 = chromosome[i]
      city2 = chromosome[(i + 1) % len(chromosome)]# apperantly %len() wraps back to starting city.
      total += distanceCalc(city1,city2)
   return total

#Sends each of the chromsome in population to tour_lenght functions one by one to calc each length then returns them and puts them in a list so we can compare or mutate later.


listOfTourLenghts = [tour_lenght(chromosome) for chromosome in population]
genCount = 0
maxgen = 100
bestTourLenght = float('inf')
noImproveCount = 0
#the conditions for stopping the generetain of new gen is eihter 100 or best not changing so we add these limits.

while(genCount < maxgen and noImproveCount < 5):
   indexOfElit = listOfTourLenghts.index(min(listOfTourLenghts))
   bestLenght = listOfTourLenghts[indexOfElit]
   elitisim = population[indexOfElit].copy()
   #we print the best of each generations best to terminal. it was asked in docx
   print(f"Generation: {genCount +1}. Best lenght: {bestLenght} ")
   if bestLenght < bestTourLenght:
      bestTourLenght = bestLenght
      noImproveCount = 0
   else:
      noImproveCount += 1
   genCount += 1      

   if noImproveCount >=5:
      print("Best solution has not changed for 5 consecuetive gen")
      break
   # making a copy of population so the original wont be harmed in case of something wrong 
   populationCopy = [c.copy() for c in population]
   lenghtCopy = listOfTourLenghts.copy()

 #seperating the elit of thsi generation so we can add it directly to the other gen
   populationCopy.pop(indexOfElit)
   lenghtCopy.pop(indexOfElit)
   halfLenght = int(len(lenghtCopy) * 0.5)
 #%50 persentcs
   first50Per = lenghtCopy[:halfLenght]
   second50Per = lenghtCopy[halfLenght:]
   first50PerPop = populationCopy[:halfLenght]
   second50PerPop = populationCopy[halfLenght:]

   nextGen = [elitisim]
 #for every chromosome minus the elite thus the -1 we get a parent from ecah selection rule and send it to crossover to create new chormosomes choom!
   for _ in range(len(population)- 1):
    parentForRank = rankSolution(first50PerPop,first50Per)
    parentForWheel = rouletteSelection(second50PerPop,second50Per)
    nextGen.append(creatingNextGeneration(parentForRank,parentForWheel))
 #%50 of the new gen for mutations
   newHalfLenght = int(len(nextGen) * 0.5)
   first50New = nextGen[1:newHalfLenght]
   second50New = nextGen[newHalfLenght:]
   insertMutation(first50New)
   randomSlide(second50New)
 #replace the population with new generation.
 #add new populations tour lenght to listoftourlegnhts
   population = nextGen
   listOfTourLenghts = [tour_lenght(chromosome) for chromosome in population]

   
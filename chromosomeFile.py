#İmported pathlib so ı can read the tsp file from my desktop.
#Tsplib95 lib imported cause its a lib built for tsp problems and helps me load the ids or "genes" in this instance.
#imported math so ı can calculate and compare between diffrend random chromosomes and decide which chromosome is bettere in fitness.

from pathlib import Path
import tsplib95
import random
import math
from RankBasedSelection import rankSolution

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

#picking the shortest so we can out it direcatly to the other genaration.
elitism = min(listOfTourLenghts)
indexOfElit = listOfTourLenghts.index(min(listOfTourLenghts))
#Removing them from popultaion both with index so first of all we can have a 99 chormosome and 
# second of all to not have diffrent index's in lists.
removingForSafety = population.pop(indexOfElit)
removingForSafety2 = listOfTourLenghts.pop(indexOfElit)
#Splitting the lists %50 percent just like in docx
halfLenght = int(len(listOfTourLenghts) * 0.5)
first50Per = listOfTourLenghts[:halfLenght]
second50Per = listOfTourLenghts[halfLenght:]
first50PerPop = population[:halfLenght]
second50PerPop = population[halfLenght:]
parentForRank = rankSolution(first50PerPop,first50Per)




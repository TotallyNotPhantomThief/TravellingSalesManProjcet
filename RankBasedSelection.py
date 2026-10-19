import random

#imported random cause we want to return a list(choromosome in this case) with visited city
#population in this function is %50 percent of the popultaion(49 list  of 100 city visited ranodmly (minus the elite one ))
#list of tour lenghts is also %50 so it can match the index number of 49 list 
#We sync 2 list like: Tour, tourlenght.
#then we sort according to the lenght thxs to key lambda x: x[1] and reverse it so it can go like desending (rank based solution requires worst outcome(longest in this problem) to rank 1)
#than we only take tour from synclist so we can use random.choices
#random choices takes and retunrs only 1 with probabilty of ranks from popSort which is the population taken to this funciton sorted according to the lenght of theri travels form worst(longest) to best(shortest)
def rankSolution(population , listOfTourLenghts):
  syncList = list(zip(population,listOfTourLenghts))
  syncList = sorted(syncList,key=lambda x: x[1],reverse=True)
  popSort = [travelList[0] for travelList in syncList]
  ranks = list(range(1, len(syncList) + 1))
  return random.choices(popSort,weights=ranks,k=1)[0]

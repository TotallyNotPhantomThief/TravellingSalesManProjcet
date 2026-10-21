import random
#in Random Slide mutation we basically get a element from the list randomly then
#we get the index of it after that we select a random index to insert it after that
#we insert that element and slide the rest of the list.
def randomSlide(nextGen):
    mutatedListRandom = []
    
    for chromosome in nextGen:
        index = random.randint(0,len(chromosome))
        genToMutate = random.choice(chromosome)
        chromosome.remove(genToMutate)
        chromosome.insert(index,genToMutate)
        mutatedListRandom.append(chromosome)
    return mutatedListRandom   

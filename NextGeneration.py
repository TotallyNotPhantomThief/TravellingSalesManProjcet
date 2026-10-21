#so first of all fuck this crossover thing like really fuck this shit.
#second of all first we select from parent 1 and add it to child 
# that we go to parent 2 of the same index and look at the gene there
# after that we go and look at parent 1 for the index of the said gene
# than we get the index of it and add the gene at that spot to chlid 
#we countinue this till we (first line of the loop) come across a non empty space of child
#in another loop since this is a crossover we gotta add from parent 2 otherwise this woudlnt be a crossfuckingover would it??
#so in second looop we go over child and whenever we come across a empty space we add a element of same index from parent 2
#yippie!!




def creatingNextGeneration(parent1,parent2):
    n = len(parent1)
    child = [None] * n
    i = 0
    while child[i] is None:
        child[i] = parent1[i]
        i = parent1.index(parent2[i])
    for i in range(len(child)):
        if child[i] is None:
            child[i] = parent2[i]
    
    return child
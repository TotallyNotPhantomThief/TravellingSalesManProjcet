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
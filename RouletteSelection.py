import random
#random.choices is literally wheel selection whicg depends on weights on the roullete wheel 
#we use 1/lenght so we can have not selecting the worse(longest) path all the time with inversesing it.
def rouletteSelection(popultaion,lenghtsofTours):
    fitness = (1/(lenght) for lenght in lenghtsofTours)
    return random.choices(popultaion,weights=fitness,k=1)[0]


import random
maps = ["Triton", 
        "Ephemeron",
        "World of Sleepers",
        "Zen", 
        "Simulacrum",
        "Nighshade",
        "Eternal Empire"]

def getMaps(n):
    selected = []
    mapsCopy = list(maps)
    if (n >= 7):
        return None
    for _ in range(n):
        j = random.randrange(0, len(mapsCopy))
        map = mapsCopy.pop(j)
        selected.append(map)
    return selected
    
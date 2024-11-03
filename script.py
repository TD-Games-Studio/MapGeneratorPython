# TODO: Générateur de map
# Projet Python a transcompiler en LuaJIT Roblox.

import random

NombreDePatternMax_MaisonPNJ = 20

PNJ_Names = [
    "Alex", "Mia", "Liam", "Nina", "Leo", 
    "Sara", "Max", "Ella", "Oscar", "Ivy",
    "Finn", "Lana", "Noah", "Lila", "Evan", 
    "Zara", "Kai", "Luca", "Maya", "Jude"
]

PNJ_Taken = []

ChoixPatternEau = random.randint(0, 0)
PatternEau = {
    0: [
        [(72.5, 1, 125), (145, 1, 15)],
        [(137.5, 1, 210), (15, 1, 155)],

        # Partie PONT [(256.5, 1, 280), (223, 1, 15)],
        [(201.5, 1, 280), (113, 1, 15)],
        [(323, 1, 280), (90, 1, 15)],

        [(360.5, 1, 393.75), (15, 1, 212.5)],
        [(151.5, 1, 402.75), (75, 1, 40)], 
        [(263, 1, 160.25), (50, 1, 45)],
        [(442.5, 1, 80.25), (115, 1, 15)],
        [(392.5, 1, 115.25), (15, 1, 55)],
        [(401, 1, 175.25), (60, 1, 65)],
    ]
}

Carte = {
    0: [
        [(0, 1, 250), (1, 1, 500)],
        [(500, 1, 250), (1, 1, 500)],
        [(250, 1, 0), (500, 1, 1)],
        [(250, 1, 500), (500, 1, 1)],
    ]
}

Maison = {
    0: []
}

Arbres = {
    0: []
}

BatimentSpecial = {
    0: []
}

def calculate_corners(position, size):
    x, y, z = position
    width, height, depth = size # height ne sert strictement a rien mais python le veut absolument parceque c'est une grosse salope
    
    dx = width / 2
    dz = depth / 2

    corners = [
        (x - dx, y, z - dz),
        (x + dx, y, z - dz),
        (x - dx, y, z + dz),
        (x + dx, y, z + dz),
    ]
    
    return corners

def is_point_in_block(x, y, z, pattern_blocks):
    point = (x, y, z)
    margin = 20

    for block in pattern_blocks:
        block_position, block_size = block
        corners = calculate_corners(block_position, block_size)
        
        min_x = min(corner[0] for corner in corners) - margin
        max_x = max(corner[0] for corner in corners) + margin
        min_y = min(corner[1] for corner in corners)
        max_y = max(corner[1] for corner in corners)
        min_z = min(corner[2] for corner in corners) - margin
        max_z = max(corner[2] for corner in corners) + margin
        
        if min_x <= point[0] <= max_x and min_y <= point[1] <= max_y and min_z <= point[2] <= max_z:
            return True
    
    return False

def is_maison_in_block(x, y, z, pattern_blocks):
    point = (x, y, z)
    margin = 15

    for block in pattern_blocks:
        block_position, block_size = block
        corners = calculate_corners(block_position, block_size)
        
        min_x = min(corner[0] for corner in corners) - margin
        max_x = max(corner[0] for corner in corners) + margin
        min_y = min(corner[1] for corner in corners)
        max_y = max(corner[1] for corner in corners)
        min_z = min(corner[2] for corner in corners) - margin
        max_z = max(corner[2] for corner in corners) + margin
        
        if min_x <= point[0] <= max_x and min_y <= point[1] <= max_y and min_z <= point[2] <= max_z:
            return True
    
    return False

def is_arbre_in_block(x, y, z, pattern_blocks):
    point = (x, y, z)
    margin = 10

    for block in pattern_blocks:
        block_position, block_size = block
        corners = calculate_corners(block_position, block_size)
        
        min_x = min(corner[0] for corner in corners) - margin
        max_x = max(corner[0] for corner in corners) + margin
        min_y = min(corner[1] for corner in corners)
        max_y = max(corner[1] for corner in corners)
        min_z = min(corner[2] for corner in corners) - margin
        max_z = max(corner[2] for corner in corners) + margin
        
        if min_x <= point[0] <= max_x and min_y <= point[1] <= max_y and min_z <= point[2] <= max_z:
            return True
    
    return False

def generateSafeZone(pb1, pb2, pb3, pb4, pb5, x_range=(0, 500), y=1, z_range=(0, 500)):
    #count = 0
    while True:
        #count = count+1
        x = round(random.uniform(*x_range))
        z = round(random.uniform(*z_range))
        
        if not is_point_in_block(x, y, z, pb1) and not is_point_in_block(x, y, z, pb2) and not is_maison_in_block(x, y, z, pb3) and not is_arbre_in_block(x, y, z, pb4) and not is_maison_in_block(x, y, z, pb4):
            #print(count)
            return x, y, z
        
def chooseUserName():
    while True:
        nomAleatoire = random.choice(PNJ_Names)

        if not nomAleatoire in PNJ_Taken:
            PNJ_Taken.append(nomAleatoire)
            return nomAleatoire

def spawnMaison():
    a = generateSafeZone(PatternEau[ChoixPatternEau], Carte[0], Maison[0], Arbres[0], BatimentSpecial[0]), (30, 1, 25) # 30, 1, 25 est la shape des maisons
    Maison[0].append(a)

    PatternAleatoireMaison = random.randint(0, NombreDePatternMax_MaisonPNJ-1)
    NomPNJ = chooseUserName()

    return str(f"{Maison[0][-1][0]}, {PatternAleatoireMaison}, {NomPNJ}")

def spawnArbre():
    b = generateSafeZone(PatternEau[ChoixPatternEau], Carte[0], Maison[0], Arbres[0], BatimentSpecial[0]), (5, 1, 5)
    Arbres[0].append(b)
    return str(f"{Arbres[0][-1][0]}")

def spawnMagasin():
    c = generateSafeZone(PatternEau[ChoixPatternEau], Carte[0], Maison[0], Arbres[0], BatimentSpecial[0]), (45, 1, 25)
    BatimentSpecial[0].append(c)
    return str(f"{BatimentSpecial[0][-1][0]}, Magasin")

print("Map Generator - BloxCrossing\nby Dodo & Téo\n\n-----------------------------")

MaisonPNJ = int(input("Combien de maison PNJ a générer (recommendé : 3) : "))
ArbresAGen = int(input("Combien d'arbre a générer : "))

print(f"\nPattern eau : {ChoixPatternEau}")
print(f"B.S. : {spawnMagasin()}")

for i in range(MaisonPNJ):
    print(f"Maison {i} : {spawnMaison()}")
for l in range(ArbresAGen):
    print(f"Arbre {l} : {spawnArbre()}")
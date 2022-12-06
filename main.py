import random

community_chest = (3,4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18)
Chance = (3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)

Choice_of_chest = input(("To choose Community chest, type: 'chest', to choose chance, type 'chance'."))

if Choice_of_chest == "chest":
  Community_Chest_Random = random.choice(community_chest)
  print(Community_Chest_Random)    

if Choice_of_chest == "chance":
  Chance_random = random.choice(Chance)
  print(Chance_random)

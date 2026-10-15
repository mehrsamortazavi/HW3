import numpy as np
recipes = np.array([
[15, 350, 2, 5],
[45, 600, 7, 10],
[10, 200, 0, 3],
[30, 450, 5, 7],
[60, 800, 8, 12]
])
recipe_names = ["Salad", "Curry", "Toast", "Pasta", "Stew"]
#1
minimum=recipes.min(axis=0)
maximum=recipes.max(axis=0)
recipes_scaled=(recipes-minimum)/(maximum-minimum)
#2
users = np.array([
[10, 250, 1, 4],
[50, 700, 8, 11],
[25, 400, 4, 6]
])
users_scaled=(users-minimum)/(maximum-minimum)
print(recipes_scaled)
print(20*"-")
print(users_scaled)
#3
d=users_scaled.reshape(3,1,4)-recipes_scaled.reshape(1,5, 4)
distances = np.sqrt(np.sum(d**2,axis=2))
#4
nearest=np.argmin(distances,axis=1)
print(recipe_names[nearest])

#5
ranking=np.argsort(distances,axis=1)
for i in range(3):
    print(f"User {i+1}:",recipe_names[ranking[i]])

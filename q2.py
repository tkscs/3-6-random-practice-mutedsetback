# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = ["cat", "dog", "rabbit", "horse", "turtle", "hamster", "guinea pig"]
# Age (integer)
age = [3, 5, 7, 1, 10, 34, 19]
# Color (at least 3 choices, string)
animalcolor = ["black", "white", "brown", "carmel", "spotted", "striped"]
# Weight (float)
weight = [18, 25, 30, 12, 43, 52, 132, 184]


animal = random.choice(animal)
age = random.choice(age)
animalcolor = random.choice(animalcolor)
weight = random.choice(weight)


# Print a summary of your pet using an f-string
print(f"Your pet is a {age} year old {animalcolor} {animal} that weighs {weight} pounds")
import random

print("Please enter number of names you want to generate: ")
number_of_names = int(input())

syllables = ["Ae", "Di", "Mo", "Fam", "dar", "kil", "glar", "tres"]

names = set()


# function for generating random name using 3 syllables
def generate_random_name(self, syllables):
    part1 = random.choice(syllables)
    part2 = random.choice(syllables)
    part3 = random.choice(syllables)

    res = part1 + part2 + part3

    return res


# looping over the name set until required number of names
while len(names) != number_of_names:
    name = generate_random_name(syllables)

    names.add(name)

print(names)

# writing contents of name set into a file
file = open("character_names.txt", "w")
for name in names:
    file.write(f"{name}\n")

file.close()

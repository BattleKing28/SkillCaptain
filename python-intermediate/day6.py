import random

print("Please enter number of names you want to generate: ")
number_of_names = int(input())

syllables = ["Ae", "Di", "Mo", "Fam", "dar", "kil", "glar", "tres"]

names = set()

while len(names) != number_of_names:
    part1 = random.choice(syllables)
    part2 = random.choice(syllables)
    part3 = random.choice(syllables)

    res = part1 + part2 + part3

    names.add(res)

print(names)

file = open("character_names.txt", "w")
for name in names:
    file.write(f"{name}\n")

file.close()

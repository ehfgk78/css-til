import random


stay = 0 
switch = 0 

for i in range(10000):
    doors = ["car", "lamb", "lamb"]
    random.shuffle(doors)

    choice = random.randrange(3)

    user = doors[choice]

    if user == "car": stay = stay + 1
    else:  switch = switch + 1

print("stay = ", stay)
print("switcy = ", switch)



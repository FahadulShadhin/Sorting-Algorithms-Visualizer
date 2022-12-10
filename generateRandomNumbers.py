from numpy.random import randint

data = randint(20, 50, 1000)
print(data)
with open("newData.txt", "w") as f:
    for x in data:
        f.write(f"{x} ")

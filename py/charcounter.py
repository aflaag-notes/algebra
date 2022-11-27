import os

t = 0

for file in os.listdir("mds"):
    with open("mds/" + file) as f:
        if file != "everything.md":
            t += len(f.read())

print("Characters:", t)

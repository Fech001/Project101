import random

answer = input("Do you want to roll a dice?")

while answer != "y":
    answer = input("Do you want to roll a dice?: ")

number = random.randint(1,6)

if number == 1:
    print("[-----]")
    print("[     ]")
    print("[  0  ]")
    print("[     ]")
    print("[-----]")

if number == 2:
    print("[-----]")
    print("[     ]")
    print("[0   0]")
    print("[     ]")
    print("[-----]")

if number == 3:
    print("[-----]")
    print("[  0  ]")
    print("[     ]")
    print("[0   0]")
    print("[-----]")

if number == 4:
    print("[-----]")
    print("[0   0]")
    print("[     ]")
    print("[0   0]")
    print("[-----]")

if number == 5:
    print("[-----]")
    print("[0   0]")
    print("[  0  ]")
    print("[0   0]")
    print("[-----]")

if number == 6:
    print("[-----]")
    print("[0   0]")
    print("[0   0]")
    print("[0   0]")
    print("[-----]")

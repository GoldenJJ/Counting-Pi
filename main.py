import math
import random
from termcolor import cprint

circle = 0
total = 0

cycle = 0

screen = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
minerror = 5
bestapprox = 0

while True:
    pointy = random.randint(0, screen)
    pointx = random.randint(0, screen)
    total += 1
    if pointy ** 2 + pointx ** 2 <= screen ** 2:
        circle += 1
    ratio = circle / total
    cycle += 1

    approx = ((ratio * 4))
    error = (abs(math.pi - (approx)))

    if cycle % 1000000 == 0:
        print(f"Cycle: {cycle} Error: {error} Approximation: {approx}")
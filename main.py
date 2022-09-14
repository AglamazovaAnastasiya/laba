height = float(input())
weight = float(input())
steps = int(input())
time = float(input())


step = height/4+0.37
distance = steps*step
V = distance/time
energy = 0.035*weight+(V**2/height)*0.029*weight
print(energy)

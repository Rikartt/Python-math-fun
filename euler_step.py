def step(derivative, coords, h):
    x = coords[0]
    y = coords[1]
    drv = eval(derivative)
    return (coords[0]+h, coords[1]+drv*h)
def askinput():
    global EQ
    global known
    global steplen
    global diff
    EQ = input("y' = ")
    known = [float(x) for x in input("Known coordinate, give as \"x,y\": ").split(",")]
    steplen = float(input("Step length(h) = "))
    diff = float(input("Distance to go in positive x-wise direction: "))
askinput()
if (diff/steplen) % 1 != 0:
    print("The distance given is not divisible by the step length? Continue with rounding? (y/n)")
    if input(": ") == "y":
        pass
    else:
        askinput()
coords = [(known[0],known[1])]
for i in range(int(diff//steplen)+1):
    coords.append(step(EQ,coords[i],steplen))
[print(coord) for coord in coords]
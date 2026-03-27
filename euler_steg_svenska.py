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
    known = [float(x) for x in input("Känd koordinat, ange som \"x,y\": ").split(",")]
    steplen = float(input("Steglängd(h) = "))
    diff = float(input("Distans att gå i x-led: "))
askinput()
if (diff/steplen) % 1 != 0:
    print("Distansen är inte delbar med steglängden! Fortsätt med avrundning? (y/n)")
    if input(": ") == "y":
        pass
    else:
        askinput()
coords = [(known[0],known[1])]
for i in range(int(diff//steplen)+1):
    coords.append(step(EQ,coords[i],steplen))
[print(coord) for coord in coords]
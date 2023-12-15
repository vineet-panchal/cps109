import math

sides = int(input("Enter the number of sides of the polygon (units):"))
print("")
# asking user for number of sides

sideLength = float(input("Enter the length of the sides (units):"))
# asking user for length of the sides

perimeter = sideLength * sides
print("The perimeter is: " + str(perimeter) + " units.")
# calculating perimeter

apothem = (sideLength / (2 * math.tan(math.pi / sides)))
print("The apothem is: " + str(apothem) + " units.")
# calculating apothem

area = 0.5 * apothem * (sides * sideLength)
print("The area is: " + "Area = {:.2f}".format(area) + " square units.")
# calculating area
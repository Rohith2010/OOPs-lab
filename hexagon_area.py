#Write a function called hexagon_area that takes the length of a side of a regular hexagon as a parameter and returns the area of the hexagon.
import math
def hex_area(side):
  area=((3*math.sqrt(3))/2)*side**2
  print('area of hexagon =',area)
hex_area(5)


area of hexagon = 64.9519052838329

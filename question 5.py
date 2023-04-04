#we will use math function for this question
import math
for angle in range(0,346,15):
    radians=math.radians(angle)
    sine=round(math.sin(radians),4)
    cosine=round(math.cos(radians),4)
    print(f"{angle}, {sine}, {cosine}")#I have used f string to get the output
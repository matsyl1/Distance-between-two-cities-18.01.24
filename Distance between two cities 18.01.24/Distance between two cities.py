# Find the distance between Oslo, Norway and Alingsås, Sweden
# "Oslo, Norway" (59.9139, 10.7522)
# "Alingsås, Sweden" (57.9300, 12.5362)

# Using Haversine Formula
from haversine import haversine, Unit
import haversine as hs

loc1 = (59.9139, 10.7522)
loc2 = (57.9300, 12.5362)
result = hs.haversine(loc1, loc2, unit=Unit.KILOMETERS)

# result as integer
result_integer = int(result)
print("The distance between Oslo and Alingsås is:", result_integer, "kms")


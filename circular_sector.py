# นายชิษณุพงศ์ เพ็งชัย - 6410742040
import math

def area_of_circular_sector(r, d):
    area = (math.radians(d))/2 * r * r
    return area

area_1 = area_of_circular_sector(10, 90)
area_2 = area_of_circular_sector(10, 180)
print(f"Area 1 = {area_1:.2f}, Area 2 = {area_2:.3f}")

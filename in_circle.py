# นายชิษณุพงศ์ เพ็งชัย - 6410742040

import math

def cal_triangle_area(a, b, c):
     s = (a + b + c)/2
     area =  math.sqrt(s * (s-a)*(s-b)*(s-c))
     return area

def cal_radius(a, b, c):
    s = (a + b + c)/2
    area =  math.sqrt(s * (s-a)*(s-b)*(s-c))
    r = area/s
    return r

def cal_circle_area(r):
    area = math.pi * r * r
    return area

def valid_triangle(a, b, c):

    if a+b > c and a+c > b and b+c > a:
        return True
    else: 
        return False



print('Welcome to Incircle of a triangle calculator.')
a, b, c = input('Input three sides of triangle: ').split()

a = float(a)
b = float(b)
c = float(c)


while valid_triangle(a, b, c) == False:
    print('>Error! Cannot form a triangle')
    a, b, c = input('Input three sides of triangle: ').split()
    a = float(a)
    b = float(b)
    c = float(c)

    if valid_triangle(a, b, c):
        break


r = cal_radius(a, b, c)
area_cir = cal_circle_area(r)
area_tri = cal_triangle_area(a, b, c)

print(f'Radius: {r:.2f}')
print(f'Circle Area: {area_cir:.2f}')
print(f'Triangle Area: {area_tri:.2f}')







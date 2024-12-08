box_on = False
map = 1
scroll_x = 0
scroll_y = 0
attack_power = 10
start_on = True
clear = False

coordinates_list = []

x_start = 1455
y_start = 190
x_end = 1635
x_step = 1.5
y_step = 1

map_0_coordinates = [
    (10, 190, 1455, 190),
    (1635, 310, 2070, 310),
    (183, 795, 1600, 795),
    (1560, 850, 1800, 850),
    (1300, 917, 1560, 917),
    (1400, 1060, 1560, 1060),
    (1605, 1115, 1717, 1115),
    (1650, 1153, 1755, 1153),
    (1695, 1188, 1772, 1188),
    (1735, 1212, 1815, 1212),
    (1540, 1240, 1740, 1240),
]

x1 = x_start
y1 = y_start
while x1 < x_end:
    x2 = x1 + x_step
    y2 = y1
    map_0_coordinates.append((int(x1), int(y1), int(x2), int(y2)))
    x1 = x2
    y1 += y_step

# 맵 1의 발판 좌표 정의
map_1_coordinates = [
    (260, 202, 1020, 202),
    (850, 277, 925, 277),
    (830, 255, 910, 255),
    (810, 234, 910, 234),
    (385, 250, 450, 250),
    (360, 275, 430, 275),
    (330, 305, 415, 305),
    (310, 383, 395, 383)
]

coordinates_list = [map_0_coordinates, map_1_coordinates]
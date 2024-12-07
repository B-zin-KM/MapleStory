coordinates_list = []

x_start = 1455
y_start = 190
x_end = 1635
x_step = 1.5
y_step = 1

map_0_coordinates = [
    (10, 190, 1455, 190),
    (1635, 310, 2070, 310)
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
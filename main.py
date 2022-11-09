import time

import cv2
import numpy as np
import random

all_point = []
G = 1
img = cv2.imread('qwq.png', -1)
cp_img = cv2.imread('qwq.png', -1)

def point_add(x, y, x_v, y_v):
    global all_point
    dic = {'x': x, 'y': y, 'x_v': x_v, 'y_v': y_v}
    all_point.append(dic)
    return 0


def show_show(event, x, y, flags, param):
    global love, img
    #img[x:x + 10, y:y + 10] = love[0:10, 0:10]
    make_point(x,y)
    flash_point()
    img = cv2.imread('qwq.png', -1)
    draw_all_point()
    #time.sleep(0.5)


def show_show_way(y, x):
    global love, img
    if y >= 502:
        y =502
    if x>= 768:
        x = 758
    img[x:x + 10, y:y + 10] = love[0:10, 0:10]


def flash_point():
    global G
    for point in all_point:
        point['x'] = point['x'] + point['x_v']
        point['y'] = point['y'] + point['y_v']
        point['y_v'] = point['y_v'] + G


def draw_all_point():
    for point in all_point:
        if point['x'] >= 502:
            x = 502
            show_show_way(x, point['y'])
            all_point.remove(point)
        elif point['y'] >= 758:
            y = 758
            show_show_way(point['x'], y)
            all_point.remove(point)

        else:
            show_show_way(point['x'], point['y'])


def make_point(x, y):
    i = 1
    while i < 3:
        vx = random.randint(-3, 3)
        vy = random.randint(-5, 0)
        point_add(x, y, vx, vy)
        i = i +1



cv2.namedWindow('img')

love = cv2.imread('front.png', 1)
love = cv2.resize(love, (10, 10), )

while True:
    try:
        cv2.imshow('img', img)
        cv2.setMouseCallback('img', show_show)
        if cv2.waitKey(1) == ord('q'):
            break
    except:
        pass
cv2.destroyAllWindows()

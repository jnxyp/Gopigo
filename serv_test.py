# coding=utf-8

import easygopigo3 as easy
import time

gpg3_obj = easy.EasyGoPiGo3()
servo = gpg3_obj.init_servo()
d_sensor = gpg3_obj.init_distance_sensor()

current_direction = 0

# servo.rotate_servo(80)
# while True:
#     print '#' * (d_sensor.read()/5)

data = []

for degree in range(15, 165, 5):
    servo.rotate_servo(degree)
    data.append(d_sensor.read() / 3)


def draw_bar_chart_horizontal(data, char='#'):
    for value in data:
        print char * value


draw_bar_chart_horizontal(data)
gpg3_obj.stop()

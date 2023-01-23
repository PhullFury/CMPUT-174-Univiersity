import math

l = 21.3
w = 26.7
h = 29.7

volume_cm = l*w*h
volume_l = volume_cm*0.001
containers = 8/volume_l

print("Numbers of containers required", math.ceil(containers))
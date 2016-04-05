import time

import pygame.camera
import pygame.image

from config import CAPTURE_DELAY_PERIOD
from process import scan_faces

file_name = None

def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()   
    except:
        print("Error writing to: " + property + " value: " + value)
 
def set_servo(angle):
    set("servo", str(angle))

def take_image():
    img = cam.get_image()
    file_name = int(round(time.time() * 1000)) + ".bmp"
    pygame.image.save(img, file_name)
    scan_faces(file_name)

if __name__ == '__main__':
    pygame.camera.init()

    if(!pygame.camera.list_cameras()):
        print "Camera not detected."

    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()

    set("delayed", "0")
    set("mode", "servo")
    set("servo_max", "180")
    set("active", "1")
     
    for angle in range(0, 180, 30):
        set_servo(angle)
        time.sleep(delay_period)
        take_image()

    pygame.camera.quit()
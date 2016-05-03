from picamera import PiCamera
import RPi.GPIO as GPIO
import time

def change_angle(self, angle):
    # calculate the needed duty cycle
    duty = float(angle) / 10.0 + 2.5

    # change the duty cycle to change the angle of the servo
    pwm.ChangeDutyCycle(duty)

def camera_init():
    # initialize the picamera
    camera = PiCamera()

    # initialize the PWM module and GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    # set up the GPIO PWM pin to be used for output and begin its execution
    pwm = GPIO.PWM(18, 100)
    pwm.start(5)

    # begin the preview of the camera so that we don't have to wait for exposure later
    camera.start_preview()

def start_scanning():
    # sweep 120 degrees at 30 degrees each time
    for x in range(0, 4):
        # change the angle of the servo
        change_angle(30 * x)

        # give time for the camera exposure and the servo to adjust
        time.sleep(3)

        # calculate the current time in milliseconds and use it as a filename when saving
        current_time_in_ms = int(round(time.time() * 1000))
        camera.capture('images/' + current_time_in_ms)
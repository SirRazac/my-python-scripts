import RPi.GPIO as GPIO
import time

led_pin = 3
wait_seconds = 1
running = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while running:
        print("LED an")
        GPIO.output(led_pin, True)
        time.sleep(wait_seconds)

        print("LED aus")
        GPIO.output(led_pin, False)
        time.sleep(wait_seconds)
except KeyboardInterrupt:
        GPIO.cleanup()
        running = False
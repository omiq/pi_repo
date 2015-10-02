import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 40

print "OK let's start!"

# PIN style numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

def blink():
    GPIO.output(LED_PIN, True)
    sleep(1)
    GPIO.output(LED_PIN, False)
    sleep(1)
    GPIO.output(LED_PIN, True)
    sleep(1)
    GPIO.output(LED_PIN, False)
    sleep(1)

print "Blink!"
blink()
blink()
blink()
GPIO.cleanup()


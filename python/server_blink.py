import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella

import RPi.GPIO as GPIO
from time import sleep

# LED_PIN = 40 if BOARD
LED_PIN = 21

print "OK let's start!"

# PIN style numbering
# GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

def blink():
    GPIO.output(LED_PIN, True)
    sleep(1)
    GPIO.output(LED_PIN, False)
    sleep(1)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    blink()
    return "Hello World!"

@app.route("/blink-blink")
def blinkblink():
    blink()
    blink()
    return "Blink. Blink"

@app.route("/beep")
def beep():
    pibrella.light.red.on()
    sleep(1)
    pibrella.light.red.off()
    pibrella.buzzer.fail()
    return "meep meep!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

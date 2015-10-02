import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella

import RPi.GPIO as GPIO
import time
from time import sleep

# LED_PIN = 40 if BOARD
LED_PIN = 21

navigation = "<h1><a href=\"/l\">[L]</a> <a href=\"/f\">[F]</a> <a href=\"/r\">[R]</a></h1>"

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
    return navigation

@app.route("/blink-blink")
def blinkblink():
    blink()
    blink()
    return navigation

@app.route("/beep")
def beep():
    pibrella.light.red.on()
    sleep(1)
    pibrella.light.red.off()
    pibrella.buzzer.fail()
    return navigation

@app.route("/f")
def f():
    pibrella.output.on()
    time.sleep(1)
    pibrella.output.off()
    return navigation

@app.route("/r")
def r():
    pibrella.output.e.on()
    time.sleep(1)
    pibrella.output.off()
    return navigation

@app.route("/l")
def l():
    pibrella.output.f.on()
    time.sleep(1)
    pibrella.output.off()
    return navigation


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

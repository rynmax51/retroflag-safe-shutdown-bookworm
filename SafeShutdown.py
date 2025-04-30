import RPi.GPIO as GPIO
import os
import time
from multiprocessing import Process

# Initialize pins
powerPin = 3    # pin 5
ledPin = 14     # TXD
resetPin = 2    # pin 13
powerenPin = 4  # pin 7

# Initialize GPIO settings
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(powerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(resetPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.HIGH)
    GPIO.setup(powerenPin, GPIO.OUT)
    GPIO.output(powerenPin, GPIO.HIGH)
    GPIO.setwarnings(False)

# Waits for button press to issue poweroff command
def poweroff():
    while True:
        if GPIO.input(powerPin) == GPIO.LOW:
            time.sleep(0.05)  # Debounce
            if GPIO.input(powerPin) == GPIO.LOW:
                os.system("sudo shutdown -h now")
                break
        time.sleep(0.1)

# Blinks the LED to signal button being pressed
def ledBlink():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        if GPIO.input(powerPin) == GPIO.LOW:
            start = time.time()
            while GPIO.input(powerPin) == GPIO.LOW:
                GPIO.output(ledPin, GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(ledPin, GPIO.HIGH)
                time.sleep(0.2)

# Resets the Pi (optional)
def reset():
    while True:
        if GPIO.input(resetPin) == GPIO.LOW:
            time.sleep(0.05)  # Debounce
            if GPIO.input(resetPin) == GPIO.LOW:
                os.system("sudo reboot")
                break
        time.sleep(0.1)

if __name__ == "__main__":
    init()
    powerProcess = Process(target=poweroff)
    powerProcess.start()
    ledProcess = Process(target=ledBlink)
    ledProcess.start()
    resetProcess = Process(target=reset)
    resetProcess.start()

    powerProcess.join()
    ledProcess.join()
    resetProcess.join()

    GPIO.cleanup()

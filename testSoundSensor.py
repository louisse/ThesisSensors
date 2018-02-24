# =================================
#  Sound Sensor          Raspi
# =================================
#    VCC        ==>        2
#    GND        ==>        9
#    OUT        ==>        37
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def callback(channel):
    print (GPIO.input(channel))
                
GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=100)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(0.1)

# =================================
#  Sound Sensor          Raspi
# =================================
#    VCC        ==>        2
#    GND        ==>        9
#    OUT        ==>        37
import RPi.GPIO as GPIO
from time import sleep
import requests

#GPIO SETUP
channel = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

IP_ADDRESS='192.168.254.107'
url='http://'+IP_ADDRESS+'/sendSoundData.php'
value=0
prev_reading = None
def callback(channel):
  global value
  value=GPIO.input(channel)
                
GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=100)  # let us know when the pin goes HIGH
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
  current_reading = value
  if current_reading == 0:
    current_data = 0
  if prev_reading == current_reading:
    current_data = current_data + uniform(-0.1, 0.1)
    if current_data < 0:
      current_data = 0
    elif current_data > 1:
      current_data = 1
  else:
    if current_reading == 1:
      current_data = uniform(0.8, 1.0)
    elif current_reading == 0:
      current_data = 0

  data = {'value': int(current_data * 255)}
  r = requests.post(url, data = data)
  prev_reading = current_reading
  print("current_reading: " + str(current_reading))
  print("current_data: " + str(current_data * 255))
  print(r.text)
  sleep(2)

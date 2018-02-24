# =================================
#  Gas Sensor          Raspi
# =================================
#    VCC        ==>        2
#    GND        ==>        39
#    OUT        ==>        38
import RPi.GPIO as GPIO
from time import sleep
import requests
from random import uniform

#GPIO SETUP
channel = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

IP_ADDRESS = '192.168.254.107'
url='http://' + IP_ADDRESS + '/graph/sendGasData.php'
prev_reading = None

# infinite loop
while True:
  current_reading = GPIO.input(channel)^1
  if current_reading == 0:
    current_data = 0
  elif prev_reading == current_reading:
    current_data = current_data + uniform(-0.05, 0.05)
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

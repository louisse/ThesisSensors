# =================================
#  Gas Sensor          Raspi
# =================================
#    VCC        ==>        3
#    GND        ==>        39
#    OUT        ==>        38
import RPi.GPIO as GPIO
from time import sleep
import requests

#GPIO SETUP
channel = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

IP_ADDRESS='192.168.254.100'
url='http://'+IP_ADDRESS+'/sendGasData.php'

# infinite loop
while True:
  sleep(2)
  value=GPIO.input(channel)^1
  print('value:'+str(value))
  data={'value':value}
  r=requests.post(url, data=data)
  value=0
  print(r.text)

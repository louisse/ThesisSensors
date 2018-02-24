# =================================
#  Lepton                 Raspi
# =================================
#    CS         ==>        24
#    MOSI       ==>        19         
#    MISO       ==>        21
#    CLK        ==>        23
#    Ground     ==>        6
#    Vin        ==>        1
#    SDA        ==>        3
#    SCL        ==>        5
from datetime import datetime
import numpy as np
import requests
import cv2
from io import BytesIO
from threading import Timer
from pylepton.Lepton3 import Lepton3

image = None

def capture(device = "/dev/spidev0.0"):
  with Lepton3(device) as l:
    a,_ = l.capture()
  cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
  np.right_shift(a, 8, a)
  return np.uint8(a)

def send(url='http://192.168.1.14/thermal/receiveData.php', interval=2.0):
  Timer(interval, send).start()
  global image
  if image is not None:
    image = BytesIO(cv2.imencode(".png", image)[1])
    image.name = datetime.now().strftime('%Y-%m-%d %H-%M-%S')+"thermal.png"
    files = {'thermal': image}
    print('sending post data')
    r = requests.post(url, files=files)
    print(r.text)

send()

while True:
  image = capture()
  cv2.imshow("video", image)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

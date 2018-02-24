
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

import time
import numpy as np
import cv2
from pylepton.Lepton3 import Lepton3

def capture(device = "/dev/spidev0.0"):
  with Lepton3(device) as l:
#    time.sleep(0.2)
    a,_ = l.capture()
  cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
  np.right_shift(a, 8, a)
  return np.uint8(a)

while True:
  image = capture()
  cv2.imshow("video", image)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

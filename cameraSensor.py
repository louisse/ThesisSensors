import cv2
import requests
from io import BytesIO
from datetime import datetime
from threading import Timer
from time import sleep

IP_ADDRESS = '192.168.254.107'
url='http://' + IP_ADDRESS + '/camera/receiveData.php'
cap = cv2.VideoCapture(0)
while(True):
  if cap.isOpened():
  # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
      frame = cv2.resize(frame, (160, 120))
      image = BytesIO(cv2.imencode('.png', frame)[1])
      image.name = datetime.now().strftime('%Y-%m-%d %H-%M-%S')+'camera.png'
      files={'camera': image}
      r = requests.post(url, files=files)
      print(r.text)

      # Display the resulting frame
      cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  sleep(2.0)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

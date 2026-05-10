from gpiozero import MotionSensor
from picamera2 import Picamera2
from datetime import datetime

pir = MotionSensor(4)
camera = Picamera2()
camera.start()

print("모션 감지 대기 중...")

while True:
    pir.wait_for_motion()
    print("모션 감지!")
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    camera.capture_file(filename)
    print(f"사진 저장: {filename}")
    pir.wait_for_no_motion()

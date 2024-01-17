class Camera:
    def __init__(self):
        print("Camera Class 실행")
        
    def __del__(self):
        print("Camera Class 종료")
    
    def start(self):
        print("start 함수 실행")
    
    def detect(self):
        print("detect 함수 실행")
    
    def classification(self):
        print("classification 함수 실행")

cam = Camera()

cam.start()
cam.detect()
cam.classification()

del cam
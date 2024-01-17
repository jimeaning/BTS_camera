class Stage:
    def __init__(self, v_flag, h_flag):
        self.v_flag = v_flag
        self.h_flag = h_flag
        print("Stage Class 실행")
        
    def __del__(self):
        print("Stage Class 종료")
    
    def start(self):
        print("start 함수 실행")
        
    def rotate(self, v_flag):
        self.v_flag = v_flag
        print("rotate 함수 실행")
        print("v_flag 값 : ", self.v_flag)
        
    def aim(self, h_flag):
        self.h_flag = h_flag
        print("aim 함수 실행")
        print("h_flag 값 : ", self.h_flag)
        
s = Stage(0, 0)

s.start()
s.rotate(0)
s.aim(0)

del s
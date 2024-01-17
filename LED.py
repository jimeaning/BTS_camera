class LED:
    def __init__(self):
        print("LED Class 실행")
        
    def __del__(self):
        print("LED Class 종료")
    
    def led_weapon(self):
        print("LED Weapon 함수 실행")
    
    def led_launch(self):
        print("LED Launch 함수 실행")
    
    def led_all_off(self):
        print("LED All Off 함수 실행")

led = LED()

led.led_weapon()
led.led_launch()
led.led_all_off()

del led
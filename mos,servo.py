import RPi.GPIO as GPIO
from time import sleep

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4, GPIO.IN)  # set GPIO 4 as input
    GPIO.setup(26, GPIO.OUT) #set pin 26 as output (servo)

def read_moisture_sensor():
    ret = False

    if GPIO.input(4)==0:
        ret = True
        print("EC level is low please water your plants soon!")

    return ret


#position [0 deg to 180 deg]
def set_servo_position(position):
    PWM = GPIO.PWM(26, 50)  # set 50Hz PWM output at GPIO26
    PWM.start(0)

    duty_cycle = (-10*position)/180 + 12
    print("position = " + str(duty_cycle))

    PWM.ChangeDutyCycle(duty_cycle)
    sleep(0.05)
    PWM.stop()


def main():
    init()
    
    if read_moisture_sensor():
        set_servo_position(90)

    GPIO.cleanup()


if __name__ == "__main__":
    main()
    
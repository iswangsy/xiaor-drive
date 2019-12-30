# coding=utf-8
import sys
import os
if __name__ == '__main__':
    sys.path.append(os.path.dirname(sys.path[0]))
import time
import _XiaoRGEEK_GPIO_ as XR
from drive import _XiaoRGEEK_GLOBAL_variable_ as glo
import Jetson.GPIO as GPIO

#######################################
#############信号引脚定义##############
#######################################
########LED口定义#################
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED0 = 10
LED1 = 9
LED2 = 25
########电机驱动接口定义#################
ENA = 13  # //L298使能A
ENB = 20  # //L298使能B
IN1 = 19  # //电机接口1
IN2 = 16  # //电机接口2
IN3 = 21  # //电机接口3
IN4 = 26  # //电机接口4
########舵机接口定义#################
########超声波接口定义#################
ECHO = 4  # 超声波接收脚位
TRIG = 17  # 超声波发射脚位
########红外传感器接口定义#################
IR_R = 18  # 小车右侧巡线红外
IR_L = 27  # 小车左侧巡线红外
IR_M = 22  # 小车中间避障红外
IRF_R = 23  # 小车跟随右侧红外
IRF_L = 24  # 小车跟随左侧红外

#########led初始化为000##########
GPIO.setup(LED0, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.HIGH)
#########电机初始化为LOW##########
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
ENA_pwm = GPIO.PWM(ENA, 1000)
ENA_pwm.start(0)
ENA_pwm.ChangeDutyCycle(100)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
ENB_pwm = GPIO.PWM(ENB, 1000)
ENB_pwm.start(0)
ENB_pwm.ChangeDutyCycle(100)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
#########红外初始化为输入，并内部拉高#########
GPIO.setup(IR_R, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR_M, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IRF_R, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IRF_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)
##########超声波模块管脚类型设置#########
GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)  # 超声波模块发射端管脚设置trig
GPIO.setup(ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 超声波模块接收端管脚设置echo


def GPIOSet(gpio):
    GPIO.output(gpio, True)


def GPIOClr(gpio):
    GPIO.output(gpio, False)


def DigitalRead(gpio):
    return GPIO.input(gpio)


def ENAset(EA_num):
    ENA_pwm.ChangeDutyCycle(EA_num)


def ENBset(EB_num):
    ENB_pwm.ChangeDutyCycle(EB_num)


def CarMotor(car_type):
    if car_type == 'xiaor':
        return Robot_Direction()


def _Motor_Forward_():
    # print ' M2-L FOR;M1-R FOR; '
    XR.GPIOSet(XR.ENA)
    XR.GPIOSet(XR.ENB)
    XR.GPIOSet(XR.IN1)
    XR.GPIOClr(XR.IN2)
    XR.GPIOSet(XR.IN3)
    XR.GPIOClr(XR.IN4)
    XR.GPIOClr(XR.LED1)
    XR.GPIOClr(XR.LED2)


def _Motor_Backward_():
    # print ' M2-L REV;M1-R REV; '
    XR.GPIOSet(XR.ENA)
    XR.GPIOSet(XR.ENB)
    XR.GPIOClr(XR.IN1)
    XR.GPIOSet(XR.IN2)
    XR.GPIOClr(XR.IN3)
    XR.GPIOSet(XR.IN4)
    XR.GPIOSet(XR.LED1)
    XR.GPIOClr(XR.LED2)


def _Motor_TurnLeft_():
    # print ' M2-L REV;M1-R FOR; '
    XR.GPIOSet(XR.ENA)
    XR.GPIOSet(XR.ENB)
    XR.GPIOSet(XR.IN1)
    XR.GPIOClr(XR.IN2)
    XR.GPIOClr(XR.IN3)
    XR.GPIOSet(XR.IN4)
    XR.GPIOClr(XR.LED1)
    XR.GPIOSet(XR.LED2)


def _Motor_TurnRight_():
    # print ' M2-L FOR;M1-R REV; '
    XR.GPIOSet(XR.ENA)
    XR.GPIOSet(XR.ENB)
    XR.GPIOClr(XR.IN1)
    XR.GPIOSet(XR.IN2)
    XR.GPIOSet(XR.IN3)
    XR.GPIOClr(XR.IN4)
    XR.GPIOClr(XR.LED1)
    XR.GPIOSet(XR.LED2)


def _Motor_Stop_():
    # print ' M2-L STOP;M1-R STOP; '
    XR.GPIOClr(XR.ENA)
    XR.GPIOClr(XR.ENB)
    XR.GPIOClr(XR.IN1)
    XR.GPIOClr(XR.IN2)
    XR.GPIOClr(XR.IN3)
    XR.GPIOClr(XR.IN4)
    XR.GPIOSet(XR.LED1)
    XR.GPIOClr(XR.LED2)


def _ENA_Speed_(EA_num):
    print ' M1_R速度变为 %d ' % EA_num
    XR.ENAset(EA_num)


def _ENB_Speed_(EB_num):
    print ' M2_L速度变为 %d ' % EB_num
    XR.ENBset(EB_num)


class Robot_Direction:
    def __init__(self):
        pass

    def forward(self):
        # print " Robot go forward %d"%motor_flag
        if (glo.motor_flag == 1) or (glo.motor_flag == 2):
            _Motor_Forward_()
        elif (glo.motor_flag == 3) or (glo.motor_flag == 4):
            _Motor_Backward_()
        elif (glo.motor_flag == 5) or (glo.motor_flag == 6):
            _Motor_TurnLeft_()
        elif (glo.motor_flag == 7) or (glo.motor_flag == 8):
            _Motor_TurnRight_()

    def back(self):
        # print " Robot go back"
        if (glo.motor_flag == 1) or (glo.motor_flag == 2):
            _Motor_Backward_()
        elif (glo.motor_flag == 3) or (glo.motor_flag == 4):
            _Motor_Forward_()
        elif (glo.motor_flag == 5) or (glo.motor_flag == 6):
            _Motor_TurnRight_()
        elif (glo.motor_flag == 7) or (glo.motor_flag == 8):
            _Motor_TurnLeft_()

    def left(self):
        # print " Robot turn left"
        if (glo.motor_flag == 1) or (glo.motor_flag == 3):
            _Motor_TurnLeft_()
        elif (glo.motor_flag == 2) or (glo.motor_flag == 4):
            _Motor_TurnRight_()
        elif (glo.motor_flag == 5) or (glo.motor_flag == 7):
            _Motor_Forward_()
        elif (glo.motor_flag == 6) or (glo.motor_flag == 8):
            _Motor_Backward_()

    def right(self):
        # print " Robot turn right"
        if (glo.motor_flag == 1) or (glo.motor_flag == 3):
            _Motor_TurnRight_()
        elif (glo.motor_flag == 2) or (glo.motor_flag == 4):
            _Motor_TurnLeft_()
        elif (glo.motor_flag == 5) or (glo.motor_flag == 7):
            _Motor_Backward_()
        elif (glo.motor_flag == 6) or (glo.motor_flag == 8):
            _Motor_Forward_()

    def stop(self):
        _Motor_Stop_()

    def M1_Speed(self, EA_num):
        _ENA_Speed_(EA_num)

    def M2_Speed(self, EB_num):
        _ENB_Speed_(EB_num)


if __name__ == '__main__':
    car_motor = Robot_Direction()
    while True:
        print("Write command")
        cmd = input()
        if cmd == "fw":
            car_motor.forward()
        if cmd == "bw":
            car_motor.back()
        if cmd == "rx":
            car_motor.right()
        if cmd == "lx":
            car_motor.left()

        time.sleep(0.1)
        car_motor.stop()

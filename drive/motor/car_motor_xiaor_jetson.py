import time
import _XiaoRGEEK_GPIO_ as XR
from drive import _XiaoRGEEK_GLOBAL_variable_ as glo


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

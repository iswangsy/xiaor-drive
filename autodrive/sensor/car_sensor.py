# coding=utf-8
import sys
import os


if __name__ == '__main__':
    sys.path.append(os.path.dirname(sys.path[0]))
import Jetson.GPIO as GPIO


def CarSensor(car_type):
    return CarSensorXiaoR(isJetson=True)


from abc import ABC, abstractmethod
import time


class CarSensorBase(ABC):
    def __init__(self):
        import Jetson.GPIO as GPIO

        self.GPIO = GPIO

        self.sensor_label = {
            self.TRIG(): "front_crash",
            self.ECHO(): "front_crash",
            self.IR_L(): "on_the_line_lx",
            self.IR_R(): "on_the_line_rx"
        }

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR_R(), GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.IR_L(), GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.TRIG(), GPIO.OUT, initial=GPIO.LOW)  # 超声波模块发射端管脚设置trig
        GPIO.setup(self.ECHO(), GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 超声波模块接收端管脚设置echo

        GPIO.setup(self.lx_line_sensor(), GPIO.IN)
        GPIO.setup(self.rx_line_sensor(), GPIO.IN)

    @abstractmethod
    def IR_R(self):
        pass

    @abstractmethod
    def IR_L(self):
        pass

    @abstractmethod
    def TRIG(self):
        pass

    @abstractmethod
    def ECHO(self):
        pass

    def front_distance(self):
        time.sleep(0.01)
        GPIO.output(self.TRIG(), GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(self.TRIG(), GPIO.LOW)
        while not GPIO.input(self.ECHO()):
            pass
        t1 = time.time()
        while GPIO.input(self.ECHO()):
            pass
        t2 = time.time()
        distance = (t2 - t1) * 340 / 2 * 100
        time.sleep(0.01)
        return distance

    def front_crash(self):
        return self.front_distance() == 1

    def rx_above_line(self):
        return self.GPIO.input(self.IR_R()) == self.GPIO.LOW

    def lx_above_line(self):
        return self.GPIO.input(self.IR_L()) == self.GPIO.LOW

    def add_callback_to_crash(self, callback):
        if self.front_distance() <= 1:
            callback = callback


    def add_callback_to_lx_line_sensor(self, callback):
        self.GPIO.add_event_detect(self.lx_line_sensor(), self.GPIO.FALLING, callback=callback)

    def add_callback_to_rx_line_sensor(self, callback):
        self.GPIO.add_event_detect(self.rx_line_sensor(), self.GPIO.FALLING, callback=callback)

    def get_channel_label(self, channel):
        return self.sensor_label[channel]

    def test(self):
        while True:
            print("distance front", self.front_distance())
            print("front crash", self.front_crash())
            print("above line rx", self.rx_above_line())
            print("above line lx", self.lx_above_line())
            time.sleep(1)

class CarSensorXiaoR(CarSensorBase):
    def __init__(self, isJetson=True):
        super(CarSensorXiaoR, self).__init__()

    def ECHO(self):
        return 4

    def TRIG(self):
        return 17

    def IR_L(self):
        return 27

    def IR_R(self):
        return 18


if __name__ == '__main__':
    carSensor = CarSensorXiaoR(isJetson=True)
    carSensor.test()

from .car_sensor import CarSensorBase


class CarSensorXiaoR(CarSensorBase):
    def __init__(self, isJetson=False, isRaspberry=False):
        super(CarSensorXiaoR, self).__init__(isJetson, isRaspberry)

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

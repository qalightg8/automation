import time


class Kettle:
    def enable(self):
        self.__power_on()
        self.__enable_ten()
        self.__check_temperature()
        self._power_off()

    def __power_on(self):
        print('Power ON')

    def __enable_ten(self):
        print('Enabling ten')

    def __check_temperature(self):
        print('Checking temperature')

    def _power_off(self):
        print('Power OFF')

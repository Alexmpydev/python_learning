"""
Создайте класс "животное". Наполните его данными и методами на свое усмотрение. Пропишите в
методах класса докстринги с описанием метода
Почитайте про Диаграммы класса. Опишите с помощью классов кухонную технику в виде диаграммы
(пример https://www.intuit.ru/EDI/23_04_17_1/1492899714-28128/tutorial/356/objects/2/files/02_05.gif).
Продумайте классы, их назначение и взаимосвязи. Реализовать с описанием свойств и методов.
* Описать все то же с помощью питона.


"""
import requests
from time import time


class Cow:
    color: str = 'Black'
    is_male: bool = False
    age: int = 2
    weight: int = 150
    name: str = None

    def __init__(self, color=color, is_male=is_male, age=age, weight=weight, name=name):
        self.color = color
        self.is_male = is_male
        self.age = age
        self.weight = weight
        self.name = name

    def sex(self):
        if self.is_male:
            return 'Это бык'
        else:
            return 'Это корова'

    def internet_call(self, address):
        req = requests.get(address)
        return print(f'Ответ сервера {req.status_code} \n содержимое {req.text[0:100]}, \n кличка животного {self.name}')

    def eat(self):
        if self.age >= 5:
            return f'Необходимо корма {self.age * 2} кг в день'
        elif self.age <= 0:
            return f'"Это мертвое животное'

        else:
            return f'Необходимо корма {self.age / 2} кг в день'

    def pregnant(self):
        if self.is_male and self.age >= 3:
            return f'Это бык, рожать не может, но может заделать {self.age * 2 + self.weight / 10} телят'
        elif self.is_male and self.age <= 3:
            return f'Это юный теленок-бычок, заделать телят еще не может'
        elif not self.is_male and self.age >= 3:
            return f'Это корова, может родить {self.weight / 5} телят'
        else:
            return f'Это корова, но рожать не может'

    def __str__(self):
        return f'Это животное возраста {self.age} лет, с цветом {self.color} и кличкой {self.name}'


class Appliances:
    price: float
    weight: float
    color: str
    country_of_origin: str
    guarantee: int = 12
    is_power: bool = False

    def __init__(self, price, weight, color, country_of_origin, guarantee=guarantee, is_power=is_power):
        self.price = price
        self.weight = weight
        self.color = color
        self.country_of_origin = country_of_origin
        self.guarantee = guarantee
        self.is_power = is_power

    def __str__(self):
        return f'Это бытовая техника {self.price} ' \
               f'Цвета {self.color} ' \
               f'производитель - {self.country_of_origin} ' \
               f'включен ли - {self.is_power}'

    def power_on(self):  # метод включения прибора
        self.is_power = True
        return f'Запитан? {self.is_power}\n Прибор включен в сеть'

    def power_off(self):  # метод выключения прибора
        self.is_power = False
        return f'Запитан? {self.is_power}\n Прибор отключен от сети'


class KitchenStaff(Appliances):
    cooking_volume: int = 100
    _cooking_temperature: int = 0

    def __init__(self, price, weight, color, country_of_origin, guarantee, cooking_volume,
                 cooking_temperature=_cooking_temperature):
        super().__init__(price, weight, color, country_of_origin, guarantee)

        self.cooking_volume = cooking_volume
        self.cooking_temperature = cooking_temperature

    def __str__(self):
        return super().__str__() + f' Рабочий объем - {self.cooking_volume}'

    def cooking_temp(self, temp=0):  # метод установки прибора
        self.cooking_temperature = temp
        print(f'Температура изменена на {self.cooking_temperature}')

    def timer_on(self, seconds=5):  # метод включения таймера прибора
        timing = time()
        while True:
            if time() - timing > seconds:
                print(self.power_on(), 'Таймер отработал')
                break

    def timer_off(self, seconds=5):  # метод выключения таймера прибора
        timing = time()
        while True:
            if time() - timing > seconds:
                print(self.power_off(), 'Таймер отработал')
                break


class Iron(Appliances):
    _temperature: int = 0

    def mode(self, regime):
        self.power_on()
        if regime == 1:
            self._temperature = 30
            print('Температура увеличена до 30')

        elif regime == 2:
            self._temperature = 50
            print('Температура увеличена до 50')

        elif regime == 3:
            self._temperature = 70
            print('Температура увеличена до 70')

        else:
            self.power_off()
            print('Прибор отключен')


class WashingMachine(Appliances):
    _temperature: int = 0
    _spins: int = 0
    _timer: int = 0

    def timer_off(self):  # метод выключения таймера прибора
        timing = time()
        while True:
            if time() - timing > self._timer:
                print(self.power_off(), 'Таймер отработал')
                break

    def mode(self, regime):  # метод выбора режима работы прибора
        self.power_on()
        if regime == 'Обычная стирка':
            self._temperature = 60
            self._spins = 600
            self._timer = 5
            self.timer_off()
            print('Прибор отработал и отключен')

        elif regime == 'Шерсть':
            self._temperature = 30
            self._spins = 300
            self._timer = 3
            self.timer_off()
            print('Прибор отработал и отключен')

        elif regime == 'Отжим':
            self._temperature = 0
            self._spins = 1200
            self._timer = 10
            self.timer_off()
            print('Прибор отработал и отключен')

        else:
            self.power_off()
            print('Прибор не был отключен')



class Combine(KitchenStaff):
    _spins: int = 0
    _timer: int = 0

    def mode(self, regime):  # метод выбора режима работы прибора
        self.power_on()
        if regime == 'Измельчить':
            self._spins = 1200
            self._timer = 5
            self.timer_off()
            print('Прибор отработал и отключен')

        elif regime == 'Накрошить':
            self._spins = 600
            self._timer = 3
            self.timer_off()
            print('Прибор отработал и отключен')

        else:
            self.power_off()


class Oven(KitchenStaff):
    temperature: int = 0

    def mode(self, regime):  # метод выбора режима работы прибора
        self.power_on()
        if regime == 1:
            self.temperature = 50
        elif regime == 2:
            self.temperature = 70
        elif regime == 3:
            self.temperature = 150
        else:
            print('Выключи плиту')


class Electro(Oven):
    voltage: int = 220

    def voltage_check(self):  # метод проверки питания сети прибора
        if self.voltage >= 220:
            self.power_on()
        else:
            self.power_off()
            print('Нет достаточного напряжения')


class Gas(Oven):
    gas_pressure: int = 600

    def pressure_check(self):  # метод првоерки давления газа в сети
        if self.gas_pressure >= 600:
            self.power_on()
            print('Горшочек вари')
        else:
            self.power_off()
            print('Звоните в 104')


class Micro(Oven):
    output_power: int = 300
    _timer: int = 0

    def mode(self, regime):  # метод выбора режима работы прибора
        self.power_on()
        if regime == 'Разморозка':
            self.output_power = 400
            self._timer = 5
            self.timer_off()
            print('Прибор отработал и отключен')

        elif regime == 'Нагрев':
            self.output_power = 1600
            self._timer = 3
            self.timer_off()
            print('Прибор отработал и отключен')
        else:
            self.power_off()


if __name__ == '__main__':
    print('1-------------------------')
    cow_1 = Cow(age=6, color='White', name='Klava')
    cow_2 = Cow(is_male=True)
    print(cow_1, '\n', cow_2)
    cow_1.internet_call('https://google.com')
    print(cow_2.eat())
    print('2-------------------------')
    ir_1 = Iron(145.5, 56.5, 'White', 'de', guarantee=True)
    ir_1.mode(3)
    ir_1.mode(0)
    print('3-------------------------')
    w1 = WashingMachine(145.5, 56.5, 'White', 'de', guarantee=True)
    w1.mode('Шерсть')
    print('4-------------------------')
    micro1 = Micro(300.5, 77.5, 'Black', 'us', guarantee=True, cooking_volume=500)
    micro1.mode('Нагрев')
    print('--------------------------')

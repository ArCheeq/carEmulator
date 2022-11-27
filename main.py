import sys
import keyboard

from sshkeyboard import listen_keyboard

from car import Car

import requests

def exit():
    res = input("Do u want to exit the programm [y/n]: ")
    if (res == 'yes' or res == 'y'):
        sys.exit()


def main():
    print("Создайте собственный автомобиль:")

    def press(key):
        if key == "up":
            print("up pressed")
        elif key == "down":
            print("down pressed")
        elif key == "left":
            print("left pressed")
        elif key == "right":
            print("right pressed")

    listen_keyboard(on_press=press)

    car_obj = {
        'bodyType': '',
        'seatsNumber': 0,
        'dimensions': [0, 0],
        'typeOfEngine': '',
        'typeOfDrive': '',
        'transmission': '',
        'mileage': 0,
        'maxSpeed': 0,
        'volumeOfTank': 0,
        'fuelСonsumption': 0,
        'currentSpeed': 0,
        'currentMileage': 0,
        'fuelLevel': 0,
        'isDrive': False
    }

    car_obj['bodyType'] = input("Введите тип кузова: ")
    car_obj['seatsNumber'] = int(input("Введите количество мест: "))
    car_obj['dimensions'] = [int(input("Введите ширину кузова: ")), int(input("Введите длину кузова: "))]
    car_obj['typeOfEngine'] = input("Введите тип двигателя: ")
    car_obj['typeOfDrive'] = input("Введите тип привода: ")
    car_obj['transmission'] = input("Введите тип трансмиссии: ")
    car_obj['mileage'] = int(input("Введите пробег автомобиля: "))
    car_obj['maxSpeed'] = int(input("Введите максимально допустимую скорость автомобиля: "))
    car_obj['volumeOfTank'] = int(input("Введите объем бака: "))
    car_obj['fuelLevel'] = car_obj['volumeOfTank']
    car_obj['fuelСonsumption'] = int(input("Введите расход топлива: "))

    res = requests.post('http://127.0.0.1:5000/car', json=car_obj)

    car = Car(car_obj['bodyType'],
              car_obj['seatsNumber'],
              car_obj['dimensions'],
              car_obj['typeOfEngine'],
              car_obj['typeOfDrive'],
              car_obj['transmission'],
              car_obj['mileage'],
              car_obj['maxSpeed'],
              car_obj['volumeOfTank'],
              car_obj['fuelСonsumption'])

    # Keys binds

    keyboard.add_hotkey('S', car.storDrive)
    keyboard.add_hotkey('Up', lambda: car.changeCurrentSpeed(1))
    keyboard.add_hotkey('Down', lambda: car.changeCurrentSpeed(-1))

    while True:
        print("The car has started to move, if you want to stop it, press the S key")
        print("Press - Arrow Up to increase speed, otherwise press - Arrow Down")
        car.startDrive(30)

        res = input("Do you want to fill the tank? [y/n]: ")
        if (res == 'yes' or res == 'y'):
            car.fillFuel(int(input("Enter the amount of fuel: ")))

        exit()


if __name__ == "__main__":
    main()

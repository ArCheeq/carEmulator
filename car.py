import time
import requests

class Car:
    bodyType = ''
    seatsNumber = 0
    dimensions = [0, 0]
    typeOfEngine = ''
    typeOfDrive = ''
    transmission = ''
    mileage = 0
    maxSpeed = 0
    volumeOfTank = 0
    fuelСonsumption = 0

    currentSpeed = 0
    currentMileage = 0
    fuelLevel = 0

    isDrive = False

    def __init__(self, bodyType, seatsNumber, dimensions, typeOfEngine, typeOfDrive, transmission, mileage, maxSpeed, volumeOfTank, fuelСonsumption):
        self.bodyType = bodyType
        self.seatsNumber = seatsNumber
        self.dimensions = dimensions
        self.typeOfEngine = typeOfEngine
        self.typeOfDrive = typeOfDrive
        self.transmission = transmission
        self.mileage = mileage
        self.maxSpeed = maxSpeed
        self.volumeOfTank = volumeOfTank
        self.fuelСonsumption = fuelСonsumption
        self.fuelLevel = volumeOfTank

    def updateMileage(self, speed, time):
        distance = round(speed*(time/3600), 4)
        self.currentMileage += distance
        self.mileage += distance
        print(f"Current mileage: {self.currentMileage}")
        self.updateFuelLevel(distance)
        requests.post('http://127.0.0.1:5000/car/currentMileage', json=self.currentMileage)

    def updateFuelLevel(self, distance):
        if (self.fuelLevel < 5):
            print("Warning - low fuel level!!!")
        if ( self.fuelLevel - (self.fuelСonsumption * distance)/100 <= 0 ):
            self.fuelLevel = 0
            print(f"Current fuel level: {self.fuelLevel}")
            requests.post('http://127.0.0.1:5000/car/fuelLevel', json=self.fuelLevel)
            self.storDrive()
            return
        self.fuelLevel -= round((self.fuelСonsumption * distance)/100, 2)
        print(f"Current fuel level: {self.fuelLevel}")
        requests.post('http://127.0.0.1:5000/car/fuelLevel', json=self.fuelLevel)

    def fillFuel(self, fuel):
        if (self.fuelLevel + fuel > self.volumeOfTank):
            self.fuelLevel = self.volumeOfTank
            print("Fuel tank is full!")
            print(f"Current fuel level: {self.fuelLevel}")
        self.fuelLevel += fuel

    def changeCurrentSpeed(self, speed):
        if (self.isDrive):
            if (self.currentSpeed < 150 or speed < 0):
                self.currentSpeed += speed
                print(f"Now speed is: {self.currentSpeed}")
                requests.post('http://127.0.0.1:5000/car/currentSpeed', json=self.currentSpeed)
            else:
                print('Speed limit reached!')
                return
            if (self.currentSpeed == 0):
                self.storDrive()

    def startDrive(self, speed):
        self.currentSpeed = speed
        self.isDrive = True
        requests.post('http://127.0.0.1:5000/car/carState', json=self.isDrive)

        print(f"The car is moving at a speed of {speed} km/h")
        while self.isDrive:
            self.updateMileage(self.currentSpeed, speed)
            time.sleep(3)

    def storDrive(self):
        if (not self.isDrive):
            print("Car is already stopped")
            return
        print("\n Car stop driving")
        self.isDrive = False
        requests.post('http://127.0.0.1:5000/car/carState', json=self.isDrive)
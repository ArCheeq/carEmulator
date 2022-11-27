import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

car = {
    'bodyType': '',
    'seatsNumber':  0,
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


@app.route('/car', methods=['GET'])
def get_car():
    return jsonify(car)


@app.route('/car', methods=['POST'])
def add_car():
    print("POST: DATA: " + str(request.get_json()))
    car = request.get_json()
    return jsonify(car, "200")


@app.route('/car/bodyType', methods=['GET'])
def get_bodyType():
    return jsonify(car['bodyType'])


@app.route('/car/seatsNumber', methods=['GET'])
def get_seatsNumber():
    return jsonify(car['seatsNumber'])


@app.route('/car/dimensions', methods=['GET'])
def get_dimensions():
    return jsonify(car['dimensions'])


@app.route('/car/typeOfEngine', methods=['GET'])
def get_typeOfEngine():
    return jsonify(car['typeOfEngine'])


@app.route('/car/typeOfDrive', methods=['GET'])
def get_typeOfDrive():
    return jsonify(car['typeOfDrive'])


@app.route('/car/transmission', methods=['GET'])
def get_transmission():
    return jsonify(car['transmission'])


@app.route('/car/maxSpeed', methods=['GET'])
def get_maxSpeed():
    return jsonify(car['maxSpeed'])


@app.route('/car/mileage', methods=['GET'])
def get_mileage():
    return jsonify(car['mileage'])


@app.route('/car/currentSpeed', methods=['GET'])
def get_currentSpeed():
    return jsonify(car['currentSpeed'])


@app.route('/car/currentSpeed', methods=['POST'])
def change_currentSpeed():
    print("POST: currentSpeed: " + str(request.get_json()))
    car['currentSpeed'] = request.get_json()
    return jsonify(car['currentSpeed'], '200')


@app.route('/car/currentMileage', methods=['GET'])
def get_currentMileage():
    return jsonify(car['currentMileage'])


@app.route('/car/currentMileage', methods=['POST'])
def change_currentMileage():
    print("POST: currentMileage: " + str(request.get_json()))
    car['currentMileage'] = request.get_json()
    car['mileage'] += request.get_json()
    print("mileage: " + str(car['mileage']))
    return jsonify(car['currentMileage'], '200')


@app.route('/car/fuelLevel', methods=['GET'])
def get_fuelLevel():
    return jsonify(car['fuelLevel'])


@app.route('/car/fuelLevel', methods=['POST'])
def change_fuelLevel():
    print("POST: fuelLevel: " + str(request.get_json()))
    car['fuelLevel'] = request.get_json()
    print("fuelLevel: " + str(car['fuelLevel']))
    return jsonify(car['fuelLevel'], '200')


@app.route('/car/carState', methods=['GET'])
def get_carState():
    return jsonify(car['isDrive'])


@app.route('/car/carState', methods=['POST'])
def change_carState():
    print("POST: carState: " + str(request.get_json()))
    car['isDrive'] = request.get_json()
    return jsonify(car['isDrive'], '200')


if __name__ == '__main__':
    app.run()
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def getWeather(city, key_api, degrees):
    # f-string
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key_api}&units={degrees}"
    response = requests.get(url)
    data_weather = response.json()
    unit = ''

    # print("Hola: ", data_weather)
    # error code
    if data_weather["cod"] == "404":
        return "City not found."
    
    temperature = data_weather["main"]["temp"]
    description = data_weather["weather"][0]["description"]

    if degrees == "imperial":
        unit = 'F'
    else:
        unit = 'C'

    # return f"The weather in {city} is {description} with a temperature of {temperature}°{unit}."
    return data_weather

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    degrees = request.args.get('degrees')
    key_api = "20f69bb11c07ec6e3c1f2e59313e3d05"

    if degrees == 'C':
        degrees = 'metric'
    else:
        degrees = 'imperial'

    result = getWeather(city, key_api, degrees)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

# HaloufApiFlask
Comment créer une API avec Flask (Python)

- Ciro Autiero / Adrian Lorenzi
- 2021-2022

## Objectif
Création d'une API permettant de visualiser et mettre à jour des données métérologique, avec le framework Flask.

## Aide
- Documentation Flask https://flask.palletsprojects.com/en/2.1.x/

## Installation

- Mise en place de l'environnement virtuel
```shell
python3 -m venv Flask_workshop
source Flask_workshop/bin/activate
```

- Installer le framework flask
```shell
pip install Flask
```

- Exécuter flask
```shell
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```

## Steps

- ***Step 1***: Créer le fichier main.py et import ces élements
```python
from flask import Flask, render_template, request, redirect, session, url_for, sessions, jsonify
import json
import requests

app = Flask(__name__)
```

- ***Step 2***: créer une route /api/meteo pour afficher "Hello World"
> localhost:5000/api/meteo

- ***Step 3***: créer un compte sur "https://www.weatherbit.io/" pour avoir une API Key pour pouvoir avec access a l'API du site. Puis stocker cette API Key dans une variable global.

- ***Step 4***: avec la route /api/meteo displayez les données de l'api du site.
```https
https://api.weatherbit.io/v2.0/current?lat=48.85&lon=2.35&key=<API_KEY>
```

- ***Step 5***: créer un dossier "templates" et un fichier "meteo.html" dans le dossier "templates"
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Weather in {{ city }}</title>
    </head>
    <body>
        <h1>Weather in {{ city }}</h1>
        <h3>The current temperature is {{ content["app_temp"] }}°C</h3>
        <h3>The current wind speed is {{ content["country_code"] }}</h3>
        <h3>The current date is {{ content["ob_time"] }}</h3>
        <h3>The current humidity is {{ content["rh"] }}%</h3>
        <h3>The current pressure is {{ content["pres"] }} mb</h3>
        <h3>The current UV index is {{ content["uv"] }}</h3>
        <h3>The current visibility is {{ content["vis"] }} km</h3>
        <h3>The current cloudiness is {{ content["clouds"] }}%</h3>
        <h3>The current precipitation is {{ content["precip"] }}%</h3>
        <h3>The current dew point is {{ content["dewpt"] }}°C</h3>
        <h3>The current wind direction is {{ content["wind_dir"] }}</h3>
        <h3>The current sunrise is {{ content["sunrise"] }}</h3>
        <h3>The current sunset is {{ content["sunset"] }}</h3>
        
    </body>
</html>
````

- ***Step 6***: créer un ficher python "locations.py" et ajoutez les éléments ci dessous.
```python
location = {
        'Paris': [48.8566, 2.3522],
        'London': [51.5074, 0.1278],
        'New York': [40.7128, -74.0059],
        'Tokyo': [35.6895, 139.6917],
        'Sydney': [-33.8688, 151.2093],
        'Beijing': [39.9042, 116.4074],
        'Rome': [41.9028, 12.4964],
        'Bangkok': [13.7563, 100.5018],
        'Seoul': [37.5665, 126.9780],
        'Mexico City': [19.4326, -99.1332],
        'Los Angeles': [34.0522, -118.2437],    
        'Shanghai': [31.2304, 121.4737],
        'Sao Paulo': [-23.5505, -46.6333],
        'Mumbai': [19.0760, 72.8777],
        'Cairo': [30.0444, 31.2357],
        'Osaka': [34.6937, 135.5022],
        'Istanbul': [41.0082, 28.9784],
        'Moscow': [55.7558, 37.6173],
        'Jakarta': [-6.1862, 106.8063],
        'Kolkata': [22.5726, 88.3639],
        'Delhi': [28.7041, 77.1025],
        'Tehran': [35.6892, 51.3890],
        'Bogota': [4.6473, -74.0962],
        'Lagos': [6.5244, 3.3792],
        'Johannesburg': [-26.2041, 28.0473],
        'Santiago': [-33.4489, -70.6693],
        'Kinshasa': [-4.3369, 15.3271],
        'Chennai': [13.0827, 80.2707],
        'Lima': [-12.0464, -77.0428],
        'North Korea': [39.1209, 125.6830],
        'Naples': [40.8412, 14.2558],
        "Nice": [43.7031, 7.2666],
        "Manhattan": [40.7831, -73.9712],
    }


def get_locations(name):
    try:
        return location[name]
    except KeyError:
        print('Location not found')
        return None
```

- ***Step 7***: créer une route /api/meteo/\<ville\> pour afficher les données météo de la ville indiquée. importez locations dans le main.py.
```python
from locations import get_locations
```

- ***Step 8***: dans le locations.py ajoutez les éléments ci dessous.
```python
key = {
        'app_temp': ["Apparent Temperature", "°C"],
        'aqi': ["AQI", " "],
        'city_name': ["City Name", " "],
        'clouds': ["Clouds", " "],
        'country_code': ["Country Code", " "],
        'datetime': ["Date and Time", " "],
        'dewpt': ["Dew Point", "°C"],
        'dhi': ["Direct Horizontal Irradiance", "W/m^2"],
        'dni': ["Direct Normal Irradiance", "W/m^2"],
        'elev_angle': ["Elevation Angle", "°"],
        'ghi': ["Global Horizontal Irradiance", "W/m^2"],
        'h_angle': ["Hour Angle", "°"],
        'lat': ["Latitude", "°"],
        'lon': ["Longitude", "°"],
        'ob_time': ["Observation Time", " "],
        'pod': ["POD", " "],
        'precip': ["Precipitation", "mm"],
        'pres': ["Pressure", "hPa"],
        'rh': ["Relative Humidity", "%"],
        'slp': ["Sea Level Pressure", "hPa"],
        'snow': ["Snow", "mm"],
        'solar_rad': ["Solar Radiation", "W/m^2"],
        'state_code': ["State Code", " "],
        'station': ["Station", " "],
        'sunrise': ["Sunrise", " "],
        'sunset': ["Sunset", " "],
        'temp': ["Temperature", "°C"],
        'timezone': ["Timezone", " "],
        'ts': ["Timestamp", " "],
        'uv': ["UV Index", " "],
        'vis': ["Visibility", "km"],
        'weather': ["Weather", " "],
        'wind_cdir': ["Wind Direction", "°"],
        'wind_cdir_full': ["Wind Direction Full", " "],
        'wind_dir': ["Wind Direction", "°"],
        'wind_spd': ["Wind Speed", "m/s"]
}


def get_info(name):
    try:
        return key[name]
    except KeyError:
        print('Key not found')
        return None
````

- ***Step 9***: créer une route /api/meteo/\<ville\>/\<info\> pour afficher les données météo specific de la ville indiquée. importez get_info dans le main.py.
> Example: /api/meteo/Naples/clouds
```python
from locations import get_locations, get_info
```

- ***Step 10***: créer un fichier info.html dans templates et ajoutez les éléments ci dessous. Puis faite en sorte de le display avec l'HTML.
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>{{city}}</title>
    </head>
    <body>
        <h1>Info in {{ city }}</h1>
        <h3>{{data[0]}} : {{content}} {{data[1]}}</h3>
    </body>
</html>
````

# Completato

> Congratulazioni sei riuscito a finire il workshop! :)


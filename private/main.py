from flask import Flask, render_template, request, redirect, session, url_for, sessions, jsonify
import json
import requests

from locations import get_locations, get_info

app = Flask(__name__)

NEW_KEY = "750a61a305654ab4a2a62f2c2d9a715a"

METEO_API_URL = "https://api.weatherbit.io/v2.0/current?lat="

def get_weather(city):
    locate = get_locations(city)
    if locate:
        url = METEO_API_URL + str(locate[0]) + "&lon=" + str(locate[1]) + "&key=" + NEW_KEY
        response = requests.get(url)
        data = response.json()
        return data
    else:
        return None

@app.route('/api/meteo')
def meteo(city):
    dictionnaire = {
        'type': 'Prévision de température',
        'valeurs': [24, 24, 25, 26, 27, 28],
        'unite': "degrés Celcius"
    }
    return jsonify(dictionnaire)

@app.route('/api/meteo2/')
def meteo2():
    response = requests.get(METEO_API_URL)
    content = json.loads(response.content.decode('utf-8'))
    if response.status_code != 200:
        return jsonify({
            'status': 'error',
            'message': 'La requête à l\'API météo n\'a pas fonctionné. Voici le message renvoyé par l\'API : {}'.format(content['message'])
        }), 500
    else:
        return jsonify(content)

@app.route('/api/meteo/<city>')
def meteo_city(city):
    content = get_weather(city)
    if content:
        return render_template('meteo.html', content=content['data'][0], city=city)
    else:
        return jsonify({
            'status': 'City not found',
            'message': 'La requête à l\'API météo n\'a pas fonctionné.' 
    }), 404

@app.route('/api/meteo/<city>/<info>')
def meteo_info(city, info):
    content = get_weather(city)
    if content:
        try:
            data = get_info(str(info))
            return render_template('info.html', content=content['data'][0][str(info)], city=city, data=data)
        except:
            return jsonify({
                'status': 'Info not found',
                'message': 'La requête à l\'API météo n\'a pas fonctionné.' 
            })  
    else:
        return jsonify({
            'status': 'City not found',
            'message': 'La requête à l\'API météo n\'a pas fonctionné.' 
        })
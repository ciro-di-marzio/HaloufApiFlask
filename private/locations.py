

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

def get_locations(name):
    try:
        return location[name]
    except KeyError:
        print('Location not found')
        return None

def get_info(name):
    try:
        return key[name]
    except KeyError:
        print('Key not found')
        return None
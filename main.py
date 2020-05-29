import requests


def get_temperature(lat, lng):
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)
    reponse = requests.get(url)
    data = reponse.json()

    try:
        """
        Faz tentativa e retona invalido caso temperatura = float or int 
        """
        if type(data.get('currently').get('temperature')) == float or int:

            temperature = data.get('currently').get('temperature')
            return int((temperature - 32) * 5.0 / 9.0)
        else:
            return "Invalid temperature"
    except ValueError:
        return data


"""
d = get_temperature(-14.235004, -51.92528)
print(d)
"""

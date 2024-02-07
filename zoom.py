import requests


class Geo:
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "format": "json"}

    def init(self, topomin_to_find):
        self.geocoder_params['geocode'] = topomin_to_find

        response = requests.get(self.geocoder_api_server, params=self.geocoder_params)
        self.json_response = response.json()

    def get_spn(self):
        coords = self.json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]['boundedBy']['Envelope']

        h = abs(float(coords['lowerCorner'].split()[0]) - float(coords['upperCorner'].split()[0]))
        w = abs(float(coords['lowerCorner'].split()[1]) - float(coords['upperCorner'].split()[1]))
        delta = f'{h},{w}'

        return delta

    def get_pos(self):
        return self.json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]["Point"]["pos"].split(" ")

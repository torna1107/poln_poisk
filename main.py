import sys
from io import BytesIO
import requests
from PIL import Image

from zoom import Goe


toponym_to_find = " ".join(sys.argv[1:])
geo = Geo(toponym_to_find)

toponym_longitude, toponym_lattitude = geo.get_pos()

delta = geo.get_spn()

map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": delta,
    "l": "map",
    'pt': f'{toponym_longitude},{toponym_lattitude},pm2dgl'
    }

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()

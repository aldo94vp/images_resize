from PIL import Image
from io import BytesIO
import requests

headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization' : 'Bearer HEREYOURTOKENOFACCESS'}
res = requests.get('https://your.url.to/get/an/image', headers=headers).content

image = Image.open(BytesIO(res))
image.save('image_old.jpeg', 'JPEG', quality=90)
# Resize image if width is major than 1000 px
a = [x/4 if image.size[0] > 1000 else x for x in image.size]
image = image.resize(a, Image.ANTIALIAS) 
image.save('image_new.jpeg', 'JPEG', quality=90)
image = Image.open('image.jpeg')

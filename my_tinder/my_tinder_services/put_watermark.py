from PIL import Image
from io import BytesIO
from my_tinder.apps import MyTinderConfig
from dating_site.settings import BASE_DIR
from django_filters import rest_framework as filters
from my_tinder.models import CustomUser
import geocoder

app_name = MyTinderConfig.name  # название приложения
watermark = 'watermark.png'  # название изображение, содержащее водяной знак
path_to_watermark = f'{BASE_DIR}/{app_name}/{watermark}'  # путь до изображения, содержащее водяной знак


def put_watermark(base_image: Image, watermark_path: str = path_to_watermark) -> BytesIO:
    if base_image.mode != 'RGBA':
        base_image = base_image.convert('RGBA')
    watermark_image: Image = Image.open(watermark_path)
    width, heigth = base_image.size
    watermark_image.thumbnail((width // 3, heigth // 3))
    destination = (width - watermark_image.size[0], 0)
    base_image.alpha_composite(watermark_image, destination)
    byte_io = BytesIO()
    base_image.save(byte_io, 'PNG')
    return byte_io


class UserFilter(filters.FilterSet):

    class Meta:
        model = CustomUser
        fields = {
            'id': ['exact'],
            'gender': ['exact'],
            'first_name': ['icontains', 'lt', 'gt'],
            'last_name': ['icontains', 'lt', 'gt']
        }


def get_lat_long(user_ip):
    g = geocoder.ipinfo(user_ip)
    latitude = g[0]
    longitude = g[1]
    return latitude, longitude

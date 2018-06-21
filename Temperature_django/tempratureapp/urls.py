from django.conf.urls import  url

from .import views

urlpatterns = [
    url(r'^convert/fahrenheit/(?P<temperature>\d+)$', views.fahrenheit, name='fahrenheit'),
    url(r'^convert/celsius/(?P<temperature>\d+)$', views.celsius, name='celsius'),
    url(r'^convert/kelvin/(?P<temperature>\d+)$', views.kelvin, name='kelvin'),
    url(r'^convert/rankine/(?P<temperature>\d+)$', views.rankine, name='rankine'),
]
from django.urls import path
from . import home


urlpatterns = [
    path('', home.homepage, name="pocetna"),
    path('brojac/', home.number, name="brStana"),
]

from django.conf.urls import url
from . import views

app_name = 'calculator'

urlpatterns = [
    url(r'^calculator/$', views.balance_calculator, name='balance_calculator'),
    url(r'^players/$', views.players_list, name='players_list'),
    url(r'^games/$', views.games_list, name='games_list'),
]

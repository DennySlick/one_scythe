from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.balance_calculator, name='balance_calculator'),
]

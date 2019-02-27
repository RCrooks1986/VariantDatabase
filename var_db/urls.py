from django.conf.urls import url, include
from var_db import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
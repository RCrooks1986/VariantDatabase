from django.conf.urls import url, include
from var_db import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^add$', views.add, name='add')
]
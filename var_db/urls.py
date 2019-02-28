from django.conf.urls import url, include
from var_db import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search_variant, name='search_variant'),
    url(r'^edit$', views.edit_variant, name='edit_variant'),
    url(r'^add$', views.add_variant, name='add_variant'),
    url(r'^upload$', views.upload_file, name='upload_file')

]
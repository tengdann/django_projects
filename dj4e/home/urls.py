from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    url(r'', views.index, name = 'index'),  
]
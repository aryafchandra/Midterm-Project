from django.urls import path

from .views import main, about

app_name = 'main'

urlpatterns = [
    path('', main, name='home'),
    path('about', about, name='about')
]

from django.urls import path

from .views import interest, main, about, interest

app_name = 'main'

urlpatterns = [
    path('', main, name='home'),
    path('about', about, name='about'),
    path('interest-form', interest)
]

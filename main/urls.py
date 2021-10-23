from django.urls import path
from .views import main, about, suggestion, interest

app_name = 'main'

urlpatterns = [
    path('', main, name='home'),
    path('about', about, name='about'),
    path('suggestion', suggestion, name='suggestion'),
    path('interest', interest, name='interest')
]

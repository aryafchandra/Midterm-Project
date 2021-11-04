from django.urls import path
from .views import main, about, profile, suggestion, signup_request, login_request, randomize, getList, CreateThread, profile_edit

app_name = 'main'

urlpatterns = [
    path('', main, name='home'),
    path('about', about, name='about'),
    path('suggestion', suggestion, name='suggestion'),
    path('profile', profile, name='profile'),
    path('signup', signup_request, name='signup'),
    path('login', login_request, name='login'),
    path('randomize', randomize, name='randomize'),
    path('inbox', getList, name = 'inbox'),
    path('inbox/create-thread', CreateThread.as_view(), name='create-thread'),
    path('edit-profile',profile_edit, name='profile')
]

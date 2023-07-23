from django.urls import path
from .views import index, advert, advert_post, login, profile, register, top

urlpatterns = [
    path('', index, name='/'),
    path('advertisement', advert, name='advert'),
    path('advertisement-pst', advert_post, name='advert_pst'),
    path('login', login, name='login'),
    path('profile', profile, name='profile'),
    path('register', register, name='register'),
    path('top-sell', top, name='top'),
]

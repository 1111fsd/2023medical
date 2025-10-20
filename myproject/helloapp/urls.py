from django.urls import path
from . import views

app_name = 'helloapp'

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('singlepage/', views.singlepage, name='singlepage'),
    path('react-hello/', views.react_hello, name='react_hello'),
    path('react-counter/', views.react_counter, name='react_counter'),
    path('react-addition/', views.react_addition, name='react_addition'),
    path('<str:name>/', views.hello_name, name='hello_name'),
]
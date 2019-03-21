from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('<int:board_pk>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('', views.index, name='index'),
]
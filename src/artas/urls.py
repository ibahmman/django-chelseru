from django.urls import path
from . import views


app_name = 'artas'
urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.new_order, name='order-new'),
]
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('seru', views.SeruViewSet)

urlpatterns = [
    path('beyr/', views.chelseru_beyr, name='chelseru-beyr'),
]

urlpatterns += router.urls
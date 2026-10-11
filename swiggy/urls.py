from django.urls import path
from . import views
urlpatterns = [
    path('', views.swiggy),
    path('swiggy/', views.swiggy2),
]
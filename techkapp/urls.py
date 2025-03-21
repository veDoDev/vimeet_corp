from django.urls import path
from . import views
from .views import redirect_to_app

urlpatterns = [
    path('',views.home, name='home'),
    path('crop/', views.crop, name='crop'),
    # path('predict_crop/', views.predict_crop, name='predict_crop'),
    # path('crop_recommendation/', views.crop_recommendation, name='crop_recommendation'),
    path('crop_tips/',views.crop_tips,name='crop_tips'),
    path('weather/',views.weather,name='weather'),
    path('counter/',views.counter,name='counter'),
    path('find_crop/',redirect_to_app, name='find_crop'),
]
from django.urls import path
from . import views

urlpatterns = [
    # Or any view you've defined in your views.py file
    path('', views.index, name='index'),  
    path('intro/', views.intro, name='intro'), 
]

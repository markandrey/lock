from django.urls import path
from start import views

app_name = 'start'

urlpatterns = [
   path('', views.index, name='home'),
]

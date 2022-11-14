from django.urls import path
from .views import *

# app_name = 'portfolio'

urlpatterns = [
    path('', index, name='home'),
    path('download-resume/', download_resume, name='download_resume')

]

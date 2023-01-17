from django.urls import path
from api.views import *

app_name = 'api'

api_path = [
    path('api/incident/create', APICreateIncidentView.as_view(), name='home'),
]

urlpatterns = [
    *api_path,
]


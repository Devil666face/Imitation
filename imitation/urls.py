from django.urls import path
from imitation.views import *

app_name = 'imitation'

home = [
    path('', HomeView.as_view(), name='home'),
    path('stat', StatisticView.as_view(), name='stat'),
    path('result', ResultView.as_view(), name='result'),
]

incident = [
    path('incident/list', IncidentListAjaxView.as_view(), name='incident_list'),
    path('incident/<int:pk>/delete', IncidentDeleteAjaxView.as_view(), name='incident_delete'),
    path('incident/create', IncidentCreateView.as_view(), name='incident_create'),
    path('incident/<int:pk>/update/legal', IncidentUpdateLegalAjaxView.as_view(), name='incident_update_legal'),
    path('incident/<int:pk>/update', IncidentUpdateAjaxView.as_view(), name='incident_update'),
    path('incident/stat', IncidentAjaxStatisticView.as_view(), name='incident_stat'),
]

category = [
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/<slug:slug>/delete', CategoryDeleteAjaxView.as_view(), name='category_delete'),
    path('category/<slug:slug>/update', CategoryUpdateAjaxView.as_view(), name='category_update'),
]

exampleincident = [
    path('exampleincident/create', ExampleIncidentCreateView.as_view(), name='exampleincident_create'),
    path('exampleincident/<int:pk>/delete', ExampleIncidentDeleteAjaxView.as_view(), name='exampleincident_delete'),
    path('exampleincident/<int:pk>/update', ExampleIncidentUpdateAjaxView.as_view(), name='exampleincident_update'),
]


urlpatterns = [
    *home,
    *incident,
    *category,
    *exampleincident,
]

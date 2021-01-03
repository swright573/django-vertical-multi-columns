from django.urls import path
from . import views

app_name = 'exercise_vmc'

urlpatterns = [
    path('even', views.EvenList.as_view(), name='even_list'),
    path('criteria', views.CriteriaList.as_view(), name='criteria_list'),
    path('defined', views.DefinedList.as_view(), name='defined_list'),
]
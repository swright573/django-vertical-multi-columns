from django.urls import path
from . import views

app_name = 'exercise_vmc'

urlpatterns = [
    path('even', views.EvenVMC.as_view(), name='even_list'),
    path('criteria', views.CriteriaVMC.as_view(), name='criteria_list'),
    path('defined', views.DefinedVMC.as_view(), name='defined_list'),
]
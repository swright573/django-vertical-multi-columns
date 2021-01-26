from django.urls import path
from . import views

app_name = 'vmcexamplesite'

urlpatterns = [
    path('', views.About.as_view(), name= 'about'),
    path('even', views.EvenVMC.as_view(), name='even_list'),
    path('criteria', views.CriteriaVMC.as_view(), name='criteria_list'),
    path('defined', views.DefinedVMC.as_view(), name='defined_list'),
    path('standard', views.StandardDjango.as_view(), name='standard_list'),
]
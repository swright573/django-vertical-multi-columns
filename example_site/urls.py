"""
Urls for the VMC Example Site

"""

from django.urls import path

from . import views

app_name = "vmcexamplesite"

urlpatterns = [
    path("", views.About.as_view(), name="about"),
    path("evensimple", views.EvenVMCSimple.as_view(), name="even_list_simple"),
    path("evencomplex", views.EvenVMCComplex.as_view(), name="even_list_complex"),
    path("criteriasimple", views.CriteriaVMCSimple.as_view(), name="criteria_list_simple"),
    path("criteriacomplex", views.CriteriaVMCComplex.as_view(), name="criteria_list_complex"),
    path("definedcomplex", views.DefinedVMC.as_view(), name="defined_list"),
    path("standard", views.StandardDjango.as_view(), name="standard_list"),
]

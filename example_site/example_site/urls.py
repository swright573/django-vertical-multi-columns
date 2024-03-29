# -*- coding: utf-8 -*-
"""
Urls for the VMC Example Site

"""

from django.urls import path  # noqa   # pylint: disable=import-error

from . import views

app_name = "vmcexamplesite"  # noqa   # pylint: disable=invalid-name

urlpatterns = [
    path("", views.About.as_view(), name="about"),
    path("evensimple", views.EvenVMCSimpleJson.as_view(), name="even_list_simple_json"),
    path("evencomplex", views.EvenVMCComplexJson.as_view(), name="even_list_complex_json"),
    path("criteriasimple", views.CriteriaVMCSimpleJson.as_view(), name="criteria_list_simple_json"),
    path("criteriacomplex", views.CriteriaVMCComplexJson.as_view(), name="criteria_list_complex_json"),
    path("definedcomplex", views.DefinedVMC.as_view(), name="defined_list"),
    path("standard", views.StandardDjango.as_view(), name="standard_list"),
]

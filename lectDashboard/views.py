from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User, auth

from .models import David_Wright_CRM_Class

# Create your views here.


class lectDashbrdView(TemplateView):
    template_name = "wrightDash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = David_Wright_CRM_Class.objects.values_list("test1", "test2")
        return context

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .models import MenuItem

# Create your views here.

def home(request):
    context = {}
    return render(request, "inventory/home.html", context)

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

# *** all functions and classes requires login *** 

class MenuItemList(ListView):
    model = MenuItem

# class InventoryList(ListView)

# class InventoryCreate(CreateView)

# class InventoryUpdate(UpdateView)

# class MenuItmeCreate(CreateView)

# class MenuItemUpdate(UpdateView)

# class PurchaseList(ListView)

# class PurchaseCreate(CreateView)

# class PurchaseUpdate(UpdateView)
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuItemForm

# Create your views here.

def home(request):
    context = {}
    return render(request, "inventory/home.html", context)

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

# *** all functions and classes requires login *** 

# ----------------------- MENU ITEM -------------------------
class MenuItemList(ListView):
    model = MenuItem

class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menuitem_add_form.html"


# ----------------------- INGREDENT -------------------------

class IngredientList(ListView):
    model = Ingredient


# ------------------- RECIPE REQURIEMENT --------------------
class RecipeRequirementList(ListView):
    model = RecipeRequirement

    def get_template_names(self):
        return "inventory/recipe_list.html"


# ----------------------- PURCHASE --------------------------

class PurchaseList(ListView):
    model = Purchase

    def get_template_names(self):
        return "inventory/report_list.html"

# class InventoryCreate(CreateView)

# class InventoryUpdate(UpdateView)

# class MenuItmeCreate(CreateView)

# class MenuItemUpdate(UpdateView)



# class PurchaseCreate(CreateView)

# class PurchaseUpdate(UpdateView)


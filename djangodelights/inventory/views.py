from django.db.models import query
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuItemForm, IngredientForm, RecipeRequirementForm, PurchaseForm

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

# class MenuItemUpdateView(UpdateView):
#     model = MenuItem
#     form_class = MenuItemForm
#     template_name = "inventory/menuitem_update_form.html"


# ----------------------- INGREDENT -------------------------

class IngredientList(ListView):
    model = Ingredient

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_add_form.html"


# ------------------- RECIPE REQURIEMENT --------------------
class RecipeRequirementList(ListView):
    model = RecipeRequirement

    def get_queryset(self):
        menuitem_title = self.kwargs["menuitem_title"]
        menuitem = MenuItem.objects.get(title=menuitem_title)
        queryset = menuitem.reciperequirement_set.all()

        return queryset

    def get_template_names(self):
        return "inventory/recipe_list.html"

class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/recipe_add_form.html"


# ----------------------- PURCHASE --------------------------

class PurchaseList(ListView):
    model = Purchase

    def get_template_names(self):
        return "inventory/report_list.html"

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/report_add_form.html"


# class InventoryCreate(CreateView)

# class InventoryUpdate(UpdateView)

# class MenuItmeCreate(CreateView)

# class MenuItemUpdate(UpdateView)



# class PurchaseCreate(CreateView)

# class PurchaseUpdate(UpdateView)


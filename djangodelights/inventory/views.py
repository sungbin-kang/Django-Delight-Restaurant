from django.db.models import query, Sum
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
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

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menuitem_update_form.html"

# class MenuItemDeleteView(DeleteView):
#     model = MenuItem
#     form_class = MenuItemForm
#     template_name = "inventory/menuitem_delete_form.html"
#     success_url = "/menu"


# ----------------------- INGREDENT -------------------------

class IngredientList(ListView):
    model = Ingredient

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_add_form.html"

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_update_form.html"

# class IngredientDeleteView(DeleteView):
#     model = Ingredient
#     form_class = IngredientForm
#     template_name = "inventory/ingredient_delete_form.html"
#     success_url = "/ingredient"


# ------------------- RECIPE REQURIEMENT --------------------
class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = "inventory/recipe_list.html"

    def get_queryset(self):
        menuitem_title = self.kwargs["menuitem_title"].replace("-", " ")
        menuitem = MenuItem.objects.get(title=menuitem_title)
        queryset = menuitem.reciperequirement_set.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menuitem_title"] = self.kwargs["menuitem_title"]
        return context

class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/recipe_add_form.html"
    
    def get_success_url(self):
        menuitem_title = self.kwargs["menuitem_title"]
        return reverse("recipe_list", kwargs={"menuitem_title": menuitem_title})

class RecipeRequirementUpdateView(UpdateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/recipe_update_form.html"

    def get_success_url(self):
        menuitem_title = self.kwargs["menuitem_title"]
        return reverse("recipe_list", kwargs={"menuitem_title": menuitem_title})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menuitem_title"] = self.kwargs["menuitem_title"]
        return context


# ----------------------- PURCHASE --------------------------

class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/purchase_add_form.html"

    # if required ingredient for menuitem not enough,
    # form input select option grayed out

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        available_menuitems = [X for X in MenuItem.objects.all() if X.available()]
        context["available_menuitems"] = available_menuitems
        return context

    def post(self, request, *args, **kwargs):

        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        
        for required_recipe in menu_item.reciperequirement_set.all():
            ingredient_in_stock = required_recipe.ingredient
            ingredient_in_stock.quantity -= required_recipe.quantity
            ingredient_in_stock.save()

        return super().post(request, *args, **kwargs)

class ReportView(TemplateView):
    template_name = "inventory/report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        purchases = Purchase.objects.all()

        revenue = purchases.aggregate(Sum("menu_item__price"))['menu_item__price__sum']

        if revenue == None:
            revenue = 0

        total_cost = 0

        for purchase in purchases:
            for recipe in purchase.menu_item.reciperequirement_set.all():
                required_quantity = recipe.quantity
                price_per_unit = recipe.ingredient.price_per_unit
                total_cost += required_quantity * price_per_unit

        profit = revenue - total_cost

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = profit

        return context

    # pass context revenue, total_cost, and profit

    # initialize purchases as all purchase objects

    # revenue is the sum of all menu price of purchases

    # for menu in purchases menu
    #     for ingredeint in menu ingredient
    #         add ingredeint unit per price times menu ingredeint required quantity
    
    # profit is revenue minus total_cost
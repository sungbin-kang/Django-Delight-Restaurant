from django import forms
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase


# ----------------------- MENU ITEM -------------------------
class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = "__all__"


# ----------------------- INGREDENT -------------------------
class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = "__all__"


# ------------------- RECIPE REQURIEMENT --------------------
class RecipeRequirementForm(forms.ModelForm):


    class Meta:
        model = RecipeRequirement
        fields = "__all__"


# ----------------------- PURCHASE --------------------------
class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = "__all__"
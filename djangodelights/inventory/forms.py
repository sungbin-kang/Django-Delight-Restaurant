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

    def __init__(self, *args, **kwargs):
        initial = kwargs["initial"]
        super(RecipeRequirementForm, self).__init__(*args, **kwargs)
        menu_item = initial["menu_item"]
        self.fields['menu_item'].queryset = MenuItem.objects.filter(title=menu_item.title)

    class Meta:
        model = RecipeRequirement
        fields = "__all__"


# ----------------------- PURCHASE --------------------------

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = "__all__"
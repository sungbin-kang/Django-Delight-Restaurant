from django import forms
from .models import MenuItem


# ----------------------- MENU ITEM -------------------------
class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = "__all__"


# ----------------------- INGREDENT -------------------------
# class InventoryForm(forms.Form)

# class PurchaseForm(forms.Form)


# ------------------- RECIPE REQURIEMENT --------------------



# ----------------------- PURCHASE --------------------------
from django.urls import path, include
from . import views

urlpatterns = [
    # path("", HomeView.as_view(), name="home"),
    path("", views.home, name="home"),
    path("account/", include("django.contrib.auth.urls")),
    path("account/signup/", views.SignUp.as_view(), name="signup"),

    # menu/
    path("menu/", views.MenuItemList.as_view(), name="menuitem_list"),
    path("menu/new", views.MenuItemCreateView.as_view(), name="menuitem_add"),

    # menu/recipe
    # change the link to each menu name
    path("menu/recipe", views.RecipeRequirementList.as_view(), name="recipe_list"),

    # ingredient/
    path("ingredient/", views.IngredientList.as_view(), name="ingredient_list"),

    # report/
    path("report/", views.PurchaseList.as_view(), name="report_list"),
]
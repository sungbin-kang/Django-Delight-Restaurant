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
    # path("menu/update/<pk>", views.MenuItemUpdateView.as_view(), name="menuitem_update"),


    # menu/recipe
    # change the link to each menu name
    path("menu/recipe", views.RecipeRequirementList.as_view(), name="recipe_list"),
    path("menu/recipe/new", views.RecipeRequirementCreateView.as_view(), name="recipe_add"),

    # ingredient/
    path("ingredient/", views.IngredientList.as_view(), name="ingredient_list"),
    path("ingredient/new", views.IngredientCreateView.as_view(), name="ingredient_add"),

    # report/
    path("report/", views.PurchaseList.as_view(), name="report_list"),
    path("report/new", views.PurchaseCreateView.as_view(), name="report_add"),
]
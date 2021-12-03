from django.urls import path, include
from . import views

urlpatterns = [
    # path("", HomeView.as_view(), name="home"),
    path("", views.home, name="home"),
    path("account/", include("django.contrib.auth.urls")),
    path("account/signup/", views.SignUp.as_view(), name="signup"),

    # menu/
    path("menu/", views.MenuItemList.as_view(), name="menuitem_list"),
    path("menu/new/", views.MenuItemCreateView.as_view(), name="menuitem_add"),
    path("menu/update/<int:pk>", views.MenuItemUpdateView.as_view(), name="menuitem_update"),
    path("menu/delete/<int:pk>", views.MenuItemDeleteView.as_view(), name="menuitem_delete"),

    # menu/recipe
    # change the link to each menu name
    path("menu/<menuitem_title>/recipe/", views.RecipeRequirementList.as_view(), name="recipe_list"),
    path("menu/<menuitem_title>/recipe/new/", views.RecipeRequirementCreateView.as_view(), name="recipe_add"),
    path("menu/<menuitem_title>/recipe/update/<int:pk>", views.RecipeRequirementUpdateView.as_view(), name="recipe_update"),
    path("menu/<menuitem_title>/recipe/delete/<int:pk>", views.RecipeRequirementDeleteView.as_view(), name="recipe_delete"),

    # ingredient/
    path("ingredient/", views.IngredientList.as_view(), name="ingredient_list"),
    path("ingredient/new/", views.IngredientCreateView.as_view(), name="ingredient_add"),

    # report/
    path("report/", views.PurchaseList.as_view(), name="report_list"),
    path("report/new/", views.PurchaseCreateView.as_view(), name="report_add"),
]
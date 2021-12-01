from django.urls import path, include
from . import views

urlpatterns = [
    # path("", HomeView.as_view(), name="home"),
    path("", views.home, name="home"),
    path("account/", include("django.contrib.auth.urls")),
    path("account/signup/", views.SignUp.as_view(), name="signup"),
    path("menu/", views.MenuItemList.as_view(), name="menuitem_list"),
    path("ingredient/", views.IngredientList.as_view(), name="ingredient_list"),
    path("report/", views.PurchaseList.as_view(), name="report_list"),
]
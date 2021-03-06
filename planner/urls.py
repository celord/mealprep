from django.urls import path

from .views import FoodCreateView, MealCreateView, create_weekly_plan, HomeView

urlpatterns = [
    path("list/", HomeView.as_view(), name="plan-list"),
    path("create/", create_weekly_plan, name="create-weekly-plan"),
    path("create_food/", FoodCreateView.as_view(), name="create-food"),
    path("create_meal/", MealCreateView.as_view(), name="create-meal"),
]

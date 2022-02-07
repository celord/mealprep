from django.contrib import admin

from .models import Food, FoodType, Meal, MealType, Plan

planner_models = [Food, FoodType, Meal, MealType, Plan]
# Register your models here.
admin.site.register(planner_models)

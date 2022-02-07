from django.shortcuts import HttpResponseRedirect  # get_object_or_404,
from django.template.response import TemplateResponse
from django.views.generic.edit import CreateView

from .forms import AddPlanForm
from .models import Food, Meal


def create_weekly_plan(request):

    template = "planner/create_weekly_plan_view.html"
    context = {}

    form = AddPlanForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/thanks/")

    context["form"] = form
    return TemplateResponse(request, template, context)


class FoodCreateView(CreateView):
    model = Food
    template_name = "planner/create_food.html"
    fields = ["food_name", "type_id", "photo"]
    success_url = "/"


class MealCreateView(CreateView):
    model = Meal
    template_name = "planner/create_meal.html"
    fields = ["meal_type", "meal_name", "photo", "foods"]
    success_url = "/"

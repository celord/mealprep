from django.core.management.base import BaseCommand

from planner.models import Food, FoodType, MealType


class Command(BaseCommand):

    help = "Load MealPrep data"

    def handle(self, *args, **kwargs):
        meal_types = ["Desayuno", "Almuerzo", "Cena", "Merienda"]

        for meal_type in meal_types:
            MealType.objects.create(type=meal_type)

        food_types = [
            "Proteina",
            "Grasa",
            "Harina",
            "Frutas",
            "Vegetales no Harinosos",
            "Lacteos",
        ]

        for food_type in food_types:
            FoodType.objects.create(type=food_type)

        proteinas = FoodType.objects.get(type="Proteina")
        foods_proteinas = [
            "Carne Molida",
            "Bistec",
            "Atun",
            "Huevos",
            "Pechuga de Pollo",
        ]

        for food in foods_proteinas:
            Food.objects.create(food_name=food, type_id=proteinas)

        harinas = FoodType.objects.get(type="Harina")
        foods_harinas = ["Caracolitos", "Arroz", "Frijoles"]

        for food_harina in foods_harinas:
            Food.objects.create(food_name=food_harina, type_id=harinas)

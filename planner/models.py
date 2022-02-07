from django.db import models
from django_extensions.db.models import TimeStampedModel


class FoodType(TimeStampedModel):

    type = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.type


class Macros(TimeStampedModel):

    protein = models.FloatField()
    sodium = models.FloatField()
    sugar = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return f"Protein: {str(self.protein)} \
                 Sodium: {str(self.sodium)} \
                 Sugar: {str(self.sugar)}  \
                 Fat: {str(self.fat)}"


class Food(TimeStampedModel):
    food_name = models.CharField(max_length=30, null=False)
    type_id = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True)
    # food_macro_id = models.ForeignKey(Macros, on_delete=models.CASCADE)

    class Meta:
        ordering = ["food_name"]

    def __str__(self):
        return self.food_name


class MealType(TimeStampedModel):

    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Meal(TimeStampedModel):

    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=20, null=False)
    photo = models.ImageField(blank=True, null=True)
    foods = models.ManyToManyField(Food)
    # meal_total_macro

    class Meta:
        ordering = ["meal_name"]

    def __str__(self):
        return self.meal_name


class History(TimeStampedModel):
    date = models.DateField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    # total_macro = models.FloatField()


class Plan(TimeStampedModel):

    date = models.DateField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    mealtype = models.ForeignKey(MealType, on_delete=models.CASCADE)
    photo = models.ImageField(
        blank=True, null=True
    )  # Signals auto update with Lunch, Dinner or BF

    def __str__(self) -> str:
        return f"{self.mealtype} for {self.date} "

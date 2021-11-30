from django.db import models

class Ingredient(models.Model):
    # name
    # quantity
    # unit
    # unit_per_price

    # def __str__
    pass

class MenuItem(models.Model):
    # title
    # price
    # image
    # description

    # def __str__
    pass

class RecipeRequirement(models.Model):
    # menu foriegn key
    # ingredient foriegn key

    # def __str__
    pass

class Purchase(models.Model):
    # menu foriegn key
    # timestamp

    # def __str__
    pass
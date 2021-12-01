from django.db import models

class Ingredient(models.Model):
    # name
    # quantity
    # unit
    # unit_per_price
    name = models.CharField(max_length=200, unique=True)
    quantity = models.PositiveBigIntegerField(default=0)
    
    gram = "g"
    litre = "l"
    ounce = "oz"
    count = ""

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
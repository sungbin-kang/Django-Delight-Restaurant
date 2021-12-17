from django.db import models
from django.urls import reverse

units_per_gram = {"grams": 1, "kilograms": 1000, "pounds": 453.592, "ounce": 28.35}

def convert_to_grams(quantity: float, unit: str):
    return quantity * units_per_gram[unit]


# --------------------------------- MENU ITEM ---------------------------------

class MenuItem(models.Model):
    """
    Represents an entry off the restaurant's menu
    """
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)
    image = models.ImageField(blank=True, null=True, upload_to="menuitem_images/")

    def get_absolute_url(self):
        return "/menu"
    
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

    def __str__(self):
        return f"title={self.title}; price={self.price}"

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(MenuItem, self).save(*args, **kwargs)


# -------------------------------- INGREDENT ----------------------------------

class Ingredient(models.Model):
    """
    Represents a single ingredient in the restaurant's inventory
    """
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)

    GRAM = "grams"
    KILOGRAM = "kilograms"
    POUND = "pounds"
    OUNCE = "ounces"
    COUNT = "counts"
    UNITS_CHOICES = {
        (GRAM, "gram"),
        (KILOGRAM, "kilogram"),
        (POUND, "pound"),
        (OUNCE, "ounce"),
        (COUNT, "count"),
    }
    unit = models.CharField(max_length=10,choices=UNITS_CHOICES, default=GRAM)

    price_per_unit = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/ingredient"

    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.price_per_unit}
        """
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
       
        return super(Ingredient, self).save(*args, **kwargs)


# --------------------------- RECIPE REQURIEMENT ------------------------------

class RecipeRequirement(models.Model):
    """
    Represents an ingredient required for a recipe for a MenuItem
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"

    def enough(self):
        return self.quantity <= self.ingredient.quantity

    def get_absolute_url(self):
        return reverse("recipe_list", kwargs={"menuitem_title": self.menu_item.title.replace(" ", "-")})
    


# --------------------------------- PURCHASE ---------------------------------

class Purchase(models.Model):
    """
    Represents a purchase of a MenuItem
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}"

    def get_absolute_url(self):
        return "/purchase"

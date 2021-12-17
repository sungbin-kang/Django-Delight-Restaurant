# Django Delight Restaurant - Django Project

# Overview
This application is to help a restaurant owner keep track of their inventory and sales. The owner starts the day with: 
- An inventory of different `Ingredient`s, their available quantity, and their prices per unit
- A list of the restaurant's `MenuItem`s, and the price set for each entry
- A list of the ingredients that each menu item requires (`RecipeRequirement`s)
- A log of all `Purchase`s made at the restaurant

The user (the restaurant owner) should be able to enter in new recipes along with their recipe requirements, and how much that menu item costs. They are also able to add to the inventory a name of an ingredient, its price per unit, and how much of that item is available.

Lastly, they are able to enter in a customer purchase of a menu item. When a customer purchases an item off the menu, the inventory should be modified to accommodate what happened, as well as recording the time that the purchase was made.

## Technical Skills
- HTML
- CSS
- Python
- Django
- Git
- Command Line

# Database Models

### `Ingredient`
This model represents an ingredient that the restaurant has in its inventory.

An ingredient should have the following fields (at least):
- **`name`**: the name of the ingredient (i.e. `flour`)
- **`quantity`**: the quantity of the ingredient available in the inventory (i.e. `4.5`)
- **`unit`**: the unit used for the ingredient (i.e. `tbsp` or `lbs`)
- **`unit_price`**: the price per unit of the ingredient (i.e. `0.05`, for a `tbsp` of `flour`)

### `MenuItem`
This model represents an item on the restaurant's menu.

A menu item should have the following fields (at least):
- **`title`**: the title of the item on the menu (i.e. `Django Juice`)
- **`price`**: the price of the item (i.e. `3.49` for a glass)

### `RecipeRequirement`
This model represents a single ingredient and how much of it is required for an item off the menu.

A recipe requirement should have the following fields (at least):
- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
- **`ingredient`**: a reference to a required ingredient for the associated menu item (i.e. a foreign key to the `Ingredient` model)
- **`quantity`**: the amount of the associated ingredient that is required to create the menu item (i.e. `1.5` ounces of `sugar` to create `Django Djaffa Cake`)


### `Purchase`
This model represents a customer purchase of an item off the menu.

A purchase should have the following fields (at least):
- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
- **`timestamp`**: a timestamp indicating the time that the purchase was recorded (i.e. a `DateTimeField`)


## Populating some sample data

### An example
Here are the ingredients for **Django Djaffa Cake**:

- 100 grams of orange jelly
- 1 large egg
- 1.5 ounces cane sugar
- 1 ounces flour
- 6 ounces milk chocolate

First, we'd create the item on our menu by creating an entry in the menu item's table:

**`MenuItem` Model**

| id  | Title              | Price |
| --- | ------------------ | ----- |
| 1   | Django Djaffa Cake | 8.25  |

In our ingredients table, we would want to ensure that all of those ingredients are present, at least.

**`Ingredient` Model**

| id  | Name           | Quantity | Unit   | Unit Price |
| --- | -------------- | -------- | ------ | ---------- |
| 1   | orange jelly   | 300      | grams  | 0.03       |
| 2   | eggs           | 12       | eggs   | 0.30       |
| 3   | cane sugar     | 50.5     | ounces | 0.65       |
| 4   | flour          | 24.5     | ounces | 0.80       |
| 5   | milk chocolate | 20.8     | ounces | 1.40       |
| 6   | feta cheese    | 3.5      | lbs    | 4.00       |

In our recipe requirements table, we would have have 5 entries:

**`RecipeRequirement` Model**

| id  | Menu Item | Ingredient | Quantity |
| --- | --------- | ---------- | -------- |
| 1   | 1         | 1          | 100.0    |
| 2   | 1         | 2          | 1.0      |
| 3   | 1         | 3          | 1.5      |
| 4   | 1         | 4          | 1.0      |
| 5   | 1         | 5          | 6.0      |

Lastly, when someone wishes to purchase a **Django Djaffa Cake**, we would allow them to select that item off the menu, add a timestamp for when they purchased it, and (after making sure we have enough of the required ingredients in our inventory), we would subtract the required quantities from the inventory and record their purchase.

**`Purchase` Model**

| id  | Menu Item | Timestamp                |
| --- | --------- | ------------------------ |
| 1   | 1         | March 4, 2021, 4:18 p.m. |


# How to use the website

## Home, Login, Signup
![alt text](https://github.com/sungbin-kang/Django-Delight-Restaurant/blob/master/resource/img-vid/home.png | width=100)
![alt text](https://github.com/sungbin-kang/Django-Delight-Restaurant/blob/master/resource/img-vid/login.png | width=100)
![alt text](https://github.com/sungbin-kang/Django-Delight-Restaurant/blob/master/resource/img-vid/signup.png | width=100)

## Add, Edit Ingredient

## Add, Edit Menu

## Make a Purchase, View Report


# Views and Templates

## Base/Home Views

`base.html`
- a base template for all the other pages to inherit from, with common styling and a navbar linking to the other pages
    - log in not required
    - if logged in, welcome prompt shown 
    - if not logged in, log in promt shown

`home.html`
- a home page
    - extends base.html
    - loggin required
    - menu bar shown horizontal view that navigate to ingredients, menu, purchases and report
- url: "" 
- url name: "home"


## List Views

`ingredeint_list.html`
- a page to view all ingredients in the inventory
    - extends home.html
    - loggin required
- url: "ingredient/" 
- url name: "ingredient_list"

`menuitem_list.html`
- a page to view the menu
    - extends home.html
    - loggin required
- url: "menu/" 
- url name: "menu_list"

`recipe_list.html`
- a page to view the menu recipe
    - extends home.html
    - loggin required
- url: "menu/<menuitem_title>/recipe" 
- url name: "recipe_list"

`purchase_list.html`
- a page to view the purchases made at the restaurant
    - extends home.html
    - loggin required
- url: "purchase/" 
- url name: "purchase_list"

`report.html`
- a page to view the profit and revenue report
    - extends home.html
    - loggin required
    - the view passes context of profit revenue to the template
- url: "report/" 
- url name: "report"

## Create Views

`menuitem_add_form.html`
- a page to add an item to the menu
    - extends home.html
    - loggin required
    - success creation redirects to "menu/"
- url: "menu/new" 
- url name: "menu_add"

`ingredeint_add_form.html`
- a page to add an ingredient to the inventory
    - extends home.html
    - loggin required
    - success creation redirects to "ingredeint/"
- url: "ingredeint/new" 
- url name: "ingredient_add"

`recipe_add_form.html`
- a page to add the recipe requirements for a menu item
    - extends home.html
    - loggin required
    - success creation redirects to "menu/<menuitem_title>/recipe/"
- url: "menu/<menuitem_title>/recipe/new" 
- url name: "recipe_add"

`purchase_add_form.html`
- a page to record a new purchase of a menu item
    - required quantity of ingredients for the menu item get subtracted from the in stock quantity
    - extends home.html
    - loggin required
    - success creation redirects to "purchase/"
- url: "purchase/new" 
- url name: "purchase_add"

## Update Views

`ingredient_update_form.html`
- a page to update the inventory for an existing ingredient
    - extends home.html
    - loggin required
    - success creation redirects to "ingredient/"
- url: "ingredeint/update/<pk>" 
- url name: "ingredeint_update"

`menu_update_form.html`
- a page to update the menu for an existing menu
    - extends home.html
    - loggin required
    - success creation redirects to "menu/"
- url: "menu/update/<pk>" 
- url name: "menuitem_update"

`recipe_update_form.html`
- a page to update the recipe for an existing menu recipe
    - extends home.html
    - loggin required
    - success creation redirects to "menu/<menuitem_title>/recipe"
- url: "menu/<menuitem_title>/update/<pk>" 
- url name: "recipe_update"

## Delete Views
`recipe_delete_form.html`
- a page to delete the recipe for an existing menu recipe
    - extends home.html
    - loggin required
    - success creation redirects to "menu/<menuitem_title>/recipe"
- url: "menu/<menuitem_title>/delete/<pk>" 
- url name: "recipe_delete"


## Ragistration Views

`login.html`
- a page to login
    - extends base.html
- url: use django.contrib.auth.urls

`signup.html`
- a page to signup
    - extends base.html
- url: "account/signup/"
- url name: "signup"
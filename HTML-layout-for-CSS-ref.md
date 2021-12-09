# HTML Layout for CSS Reference



## Base/Home Views

### `base.html`
- <head>
    - contains `base.css` stylesheet
- <body>
    - <div> class="header"
        - <h1>
            - <a> id="home-icon"
        - <h2> Welcome prompt
        - <button> id="button"

### `home.html`
- <div> class="menu-bar"



## List Views


### `menuitem_list.html`
- <div> class="menuitem-list"
    - <h2> Menu
    - <button> id="add-button" links to menuitem_add_form
    - <ul>
        - <il>
            - <img>
                - <a> id="view-button" darkens the image and link to view the recipe
            - menu title
            - menu price
            - <button> id="edit-button" links to menuitem_update_form


### `recipe_list.html`
- <div> class="recipe-list"
    - <h3>Recipe
    - <button> id="add-button" links to recipe_add_form
    - <ul>
        - <il>
            - required ingredient for the recipe
            - required quantity for the recipe
            - <button> id="edit-button" links to recipe_update_form


### `ingredeint_list.html`
- <div> class="ingredient-list"
    - <h3>Ingredients
    - <button> id="add-button"
    - <ul>
        - <il>
            - ingredient name
            - in stock quantity
            - grayed out text if out of stock
            - <button> id="edit-button"


### `purchase_list.html`
- <div> class="purchase-list"
    - <h3> Purchases
    - <button> id="add-button"
    - <ul>
        - <il>
            - purchased menuitem
            - purchased timestamp


### `report.html`
- <div> class="report"
    - <h3> Report
    - <ul>
        - <il>
            - Revenue
            - Profit





## Create Views

### `menuitem_add_form.html`
- <div> class="menuitem-add"
    - <h3> Add New Menu Item
    - <form>
        - <input> id="add-button"


### `recipe_add_form.html`
- <div> class="recipe-add"
    - <h3> Add New Ingredient for the Menu Recipe
    <!-- Work on this feature... -->
    - <img>
    - <form>
        - <input> id="add-button"
    


### `ingredeint_add_form.html`
- <div> class="ingredient-add"
    - <h3> Add New Ingredient Item
    - <form>
        - <input> id="add-button"


### `purchase_add_form.html`
- <div> class="purchase-add"
    - <h3> Purchase Menu Item
    - <form>
        - <label>
        - <selection>
        - <option>
            - Show all options but gray out unavailable menu item
        - <input> id="add-button"




## Update Views

### `menu_update_form.html`
- <div> class="menuitem-update"
    - <h3> Update Menu
    - <form>
        - <input> id="update-button"


### `recipe_update_form.html`
- <div> class="recipe-update"
    - <h3> Update Quantity
    - <form>
        - <input> id="update-button"
        - <button> id="delete-button"


### `ingredient_update_form.html`
- <div> class="ingredient-update"
    - <h3> Update Ingredient
    - <form>
        - <input> id="update-button"


<!-- Add Delete Views section to README.md -->

## Delete Views

### `recipe_delete_form.html`
- <div> class="recipe-delete"
    - <h3> Delete item from menu
    - <form>
        - <input> id="delete_button"


## Ragistration Views

### `login.html`


### `signup.html`

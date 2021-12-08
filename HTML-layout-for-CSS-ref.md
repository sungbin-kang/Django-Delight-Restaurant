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
    - <h3> Purchase
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

### `recipe_add_form.html`


### `menuitem_add_form.html`


### `ingredeint_add_form.html`


### `purchase_add_form.html`




## Update Views


### `menu_update_form.html`


### `recipe_update_form.html`


### `ingredient_update_form.html`




## Ragistration Views

### `login.html`


### `signup.html`

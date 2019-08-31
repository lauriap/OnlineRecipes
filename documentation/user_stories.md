# User stories for Online Recipes

## User types

### 'User'

'User' is the only user type used for this application apart from the Admin. The User has access to the application via a webpage and is able to perform all tasks available on the website (see below).

### 'Admin'

Admin has all the rights that a User has and on top of that has access to the source code and is thus able to carry out changes to the website and application.

Admin can also add and remove Users from the database as well as modify the database to her liking through the database terminal.


## User tasks

### Signing up for the site

As a User, I am able to insert my name, nickname and password to sign up for the site. Some of the functions on the site are limited to registered users only.

SQL-query example:

```
INSERT INTO Account(id, date_created, date_modified, name, username, password)
    VALUES (1, 2019-08-30 14:46:15, 2019-08-30 14:16:15, "Namala Name", "namalacook", "mypassword");
```

The id, date_created and date_modified are created automatically, so the user is only inputting a name, username and password.

### Logging in and logging off

As a User, I am able to log in to and log off from the website using my own nickname and password.

SQL-query example for selecting a specific user's name (user id here is 1) from the database:

```
SELECT name FROM Account
    WHERE account.id = 1;
```

### Adding recipes to the database

As a User, I am able to add my own recipes to the database. Adding recipes includes being able to add ingredients, ingredient amounts, recipe name, time required and instructions.

**SQL-query examples**

Inserting the recipe:

```
INSERT INTO Recipe (id, name, timeNeeded, instructions, user_id)
    VALUES (2, "Example recipe", 15, "Cook the ingredients and enjoy.", 1);
```

Inserting the recipe ingredients pertaining to the recipe created above:

```
INSERT INTO Recipe_ingredient (recipe_id, ingredient_id, amount)
    VALUES(2, 3, "150 g");

INSERT INTO Recipe_ingredient (recipe_id, ingredient_id, amount)
    VALUES(2, 4, "3 spoonfuls");

INSERT INTO Recipe_ingredient (recipe_id, ingredient_id, amount)
    VALUES(2, 5, "3 dl");
```

### Listing recipes

As a User, I am able to list all recipes on the webpage.

SQL query example:

```
SELECT id, name, timeNeeded, instructions FROM Recipe;
```

### Updating a recipe

As a User, I am able to update a previously added recipe, including all the variables that were available to me when adding a recipe.

SQL query example (updating recipe name, required time and ingredient amount, recipe id here is 3 and ingredient id 5):

```
UPDATE Recipe
    SET name = "Turkey pudding", timeNeeded = 15
    WHERE id = 3;

UPDATE Recipe_Ingredient
    SET amount = "1.5 litres"
    WHERE recipe_id = 3 AND ingredient_id = 5;
```

### Deleting a recipe

As a User, I am able to delete a recipe based on its id. The list of recipe names and their ids are provided with the delete recipe site template.

**SQL query examples**

Deleting the recipe ingredients (recipe id here is 3):

```
DELETE FROM Recipe_Ingredient
    WHERE recipe_id = 3;
```

Deleting the recipe itself:

```
DELETE FROM Recipe
    WHERE id = 3;
```

### Viewing a recipe

As a User, I am able to view a single recipe with all its related information, e.g. name, ingredients, instructions, time required etc.

**SQL query example**

Querying recipe information (recipe id here is 3)

```
SELECT name, timeNeeded, instructions FROM Recipe
    WHERE id = 3;
```

Querying recipe ingredients:

```
SELECT Ingredient.name, Recipe_Ingredient.amount FROM Ingredient
JOIN Recipe_Ingredient ON Ingredient.id = Recipe_Ingredient.ingredient_id
WHERE Recipe_Ingredient.recipe_id = 3;
```

### CRUD operations for ingredients

As a User, I am able to create, read ( = list), update and delete ingredients in the same vein as described above for recipes.

**SQL-query examples**

Creating an ingredient:

```
INSERT INTO Ingredient (id, name)
    VALUES (1, "Broccoli");
```

Showing an ingredient (ingredient id is 6):

```
SELECT name FROM Ingredient
    WHERE id = 6;
```

Updating an ingredient:

```
UPDATE Ingredient
    SET name = "Sage"
    WHERE id = 6;
```

Deleting an ingredient:

```
DELETE FROM Ingredient
    WHERE id = 6;
```

### Listing top contributors

As a User, I am able to list all the users sorted by the amount of recipes they have contributed to the site.

SQL query example:

```
SELECT Account.id, Account.name, COUNT(Recipe.id) AS RecipeCount FROM Account
    LEFT JOIN Recipe ON Recipe.account_id = Account.id
    GROUP BY account.id, account.name
    ORDER BY RecipeCount;
```

### Getting additional information about the recipes

As a User, I am able to additional information about the recipes on the site, including the most popular ingredient and the total number of recipes.

**SQL-query examples**

Querying the number of recipes on the site:

```
SELECT Count(Recipe.id) FROM RECIPE;
```

Querying the most popular ingredient used in the recipes:

```
SELECT Ingredient.name, COUNT(Recipe_Ingredient.id) FROM Ingredient
    LEFT JOIN Recipe_Ingredient ON Ingredient.id = Recipe_Ingredient.ingredient_id
    GROUP BY ingredient.name;
```

## Admin tasks

### Same usability as with User

As an Admin, I am able to carry out all the same tasks as a User is.

### Database operations

As an Admin, I am able to manually modify the database, including users, ingredients and recipes, through the terminal.


##List of possible future functionalities

As the amount of time available for the project was limited, all functionalities that I had in mind were not implemented. These include, among others, the following:

- search tools for recipes based on available ingredients, recipe name etc.
- dynamic forms, i.e. no limit to the amount of ingredients one can have in a recipe, but instead a dynamic number of ingredients that the User could adjust herself
- recipe rating system
- recipe of the month based on the highest new ratings given that month

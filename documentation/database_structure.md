#Database CREATE TABLE -files

##Ingredient table

CREATE TABLE ingredient (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

##Recipe table

CREATE TABLE recipe (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	"timeNeeded" INTEGER NOT NULL, 
	instructions VARCHAR(1000) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

##Account table

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
)

##Recipe_Ingredient table

CREATE TABLE recipe_ingredient (
	id INTEGER NOT NULL, 
	amount VARCHAR(144) NOT NULL, 
	recipe_id INTEGER NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipe (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredient (id)
)


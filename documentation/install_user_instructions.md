# Installing instructions for Online Recipes, Ubuntu Linux

## Installing the necessary files

Install the following programs to your computer. Attached you will also find some basic commands related to the tools:

- Python 3.5 (or newer), type the following commands to Ubuntu terminal:
	- sudo apt update
	- sudo apt install python3-pip
	- turning on python: python
	- running python programs: python programname.py

- Python virtual environment
	- sudo pip3 install virtualenv 
	- you can activate your python virtual environment by using the command "virtualenv venv", where "venv" is the name of your virtual environment

- PostgreSQL
	- apt-get install postgresql postgresql-contrib
	- set PostgreSQL to start upon server boot: update-rc.d postgresql enable
	- start PostgreSQL: service postgresql start
	- logging into the default postgres user: postgres
	- new prompt: psql
	- exiting: \q

- Git
	- download from https://git-scm.com/downloads/
	- follow the installer
	- create a profile in GitHub: https://github.com/

- Heroku
	- follow the installer guide at https://devcenter.heroku.com/articles/heroku-cli

## Cloning the project and adding a virtual environment

- open Ubuntu terminal
- clone the Online Recipes project from GitHub
	- enter a destination folder
	- git clone https://github.com/lauriap/OnlineRecipes

- create a virtual environment
	- python3 -m venv venv
	- activate venv: source venv/bin/activate
	- install Flask: pip install Flask
	- updating pip: pip install --upgrade pip

## Moving the project to Heroku and accessing it globally

- add a web server (Gunicorn): pip install gunicorn
- update requirements.txt in project root folder: pip freeze | grep -v pkg-resources > requirements.txt
- create a heroku for project: heroku create project-name-here
- add git to heroku: git remote add heroku https://github.com/lauriap/OnlineRecipes
- send project to heroku:
	- git add .
	- git commit -m "Initial commit"
	- git push heroku master
- the project is now available at your-project-name.herokuapp.com/

## Running the project locally

- enter the project root folder
- type: python run.py
- open the local address given in the terminal output


# User instructions for Online Recipes

## Registering and logging in

- You can find the links for registering and logging in in the upper right hand corner of the page
	- a name, nickname and password are required
	- to delete your profile, please contact system administration at onlinerecipes@gmail.com

## Using the website

Online Recipes provides the users with a possibility explore recipes written by the Online Recipes community as well as adding her own recipes for others to view. The website enables adding, listing, updating and deleting ingredients and recipes. The features can be accessed from the menu bar in the top edge of the website.

Once a recipe is created, the recipe can be viewed by selecting it from the recipe list. Additionally, once a view of a single recipe has been opened, the user is given the choice of editing the recipe. At an early stage of the project, it is possible to update both your own and others' recipes. This feature will be monitored closely and if it is being misused, it will be removed.

The website also tracks the top contributors to the site: The more recipes you contribute, the higher you will be on the top list! Users have the option of removing redundant or possibly offensive content from the site. The site will also be monitored by the admin for misconduct.

We wish you enjoy using Online Recipes - enjoy!

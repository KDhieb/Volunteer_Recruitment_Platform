# Volunteer Recruitment Platform - Lend A Hand
2020 Vanhacks Project (1st Place)
--

This project is the continuation of my 2020 VanHacks project. The repository contains the code needed to launch a volunteer recruitment website for non-profits.It can also be tweaked to suit different project needs. 

# Purpose
To develop a solution for non-profits to quickly find and recruit eager volunteers for different roles and make volunteering opportunities more accessible to people, allowing others to quickly begin helping their community. 

# Features
* Non-profits can create an account and profile, post new listings, and track volunteers who sign up.
* Roles can be organized based on different commitment levels (one-time, weekly, and monthly roles). 
* Volunteers can create a profile, and search for roles based on a keyword, commitment level and location.

# Technology
The website relies on Django for the backend, with SQLite for the database. 

# How to use:
1. Clone Repo
2. In **settings.py**, be sure to setup Django's **SECRET_KEY** variable. It is recommended to use an environment variable or untracked **.txt** file to store the code as to avoid writing it directly in the file. 
3. Setup virtual environment using `virtualenv venvname`.
4. Install all necessary libraries in **requirements.txt**.
5. To initialize the models and database, first use `python manage.py makemigrations` followed by `python manage.py migrate`.
6. To launch the site locally, use `python manage.py runserver`.
7. In **settings.py**, make `DEBUG** = True` and `ALLOWED_HOSTS = ['localhost', '127.0.0.1']`.

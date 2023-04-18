# Getting started

Together we are going to build our repository!

## Frameworks we picked

- Frontend
  - React (JavaScript or TypeScript?)
  - Mapping library (Mapbox or Leaflet?)
- Backend
  - Django
  - PostgeSQL (comes out of the box)
  - PostGIS (also out of the box)
- Containerization
  - Docker (this will make setup and deployment easier)

## Setup steps

### General environment

We want to start with a .gitignore, a .env, and or source code directory:

```sh
touch .gitignore
mkdir src
```

In .gitignore add:

```
# config
.env

# macOS
.DS_Store

# JS
node_modules/

# React
src/app/build/

# Django
src/django/static
src/django/db.sqlite3
```

Then run `touch .env`

### React

Use Vite to create our React app
Requires npm, but once docker is setup, it will handle that
From: https://vitejs.dev/guide/

```sh
cd src/
# From the source code folder (third-places/src)
# If you're note sure check with pwd
npm create vite@latest app --template react

# Choose React and Javascript (Typescript?)

# Go into the react source folder and create a components folder for later
cd app/src

mkdir components

# Go back to third-places/src
cd ../..
```

We can then run the `server` command in the output and browse at `http://localhost:XXXX` to see the basic page

### Django

From: https://docs.djangoproject.com/en/4.2/intro/tutorial01/

```sh
# From thirdplaces/src (check with pwd)

# Create Django project
# Basic setup gets us manage.py and ability to run the server
django-admin startproject thirdplaces

# The structure will look like src/thirdplaces/thirdplaces
# But it will help to rename src/thirdplaces to src/django which will have in it: api/ thirdplaces/ manage.py

cd thirdplaces

# Create API 
# This is where we will create our MVC api app
python3  manage.py startapp api

# Go back to third-places
cd ../../
```

We can now add the view to api/views.py:

```py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")
```

We can add our urls to api/urls.py:

```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

```

And we can add the URL to thirdplaces/urls.py:

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
]
```

And see that response by running `python3 src/django/manage.py runserver` and browsing `http://localhost:8000/api/`

### Docker

We will create an issue to containerize this

### Documentation

We need to add to the setup instructions how to run the app. This will change once we have the container set up.
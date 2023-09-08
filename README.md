
Shop Maps
=========

This is a web application to display a map with markers for shops based on their location.

Features
--------

*   Display an interactive map with shop markers using Folium
*   API to create, read, update, and delete shops in a database
*   Automated map generation showing all shops

Technologies
------------

*   Python
*   FastAPI - web framework
*   Folium - generate maps
*   Deta - serverless database

Project Structure
-----------------

Copy code

`./app |-- api/ |   |-- routes.py - define API routes   | |-- models/ |   |-- shop.py - Shop data models | |-- services/ |   |-- maps.py - map generation functions | |-- database/ |   |-- crud.py - functions to access database | main.py - create FastAPI app`

Getting Started
---------------

### Prerequisites

*   Python 3.6+
*   Pipenv or venv for virtual environments

### Installation

1.  Clone the repository

<!---->

Copy code

`git clone repo`

2. Install dependencies

<!---->

Copy code

`pipenv install`

3. Create a Deta base

*   Sign up for a [Deta account](https://deta.sh)
*   Create a micro base called `shops`
*   Add Base key to `.env` file

4.  Run the API

<!---->

Copy code

`pipenv run uvicorn main:app`

The API will be running at `http://127.0.0.1:8000`.

API Reference
-------------

The API endpoints are:

### Get all shops

Copy code

`GET /shops`

### Get single shop

Copy code

`GET /shops/{id}`

### Create shop

Copy code

`POST /shops`

### Update shop

Copy code

`PUT /shops/{id}`

### Delete shop

Copy code

`DELETE /shops/{id}`

### Get map

Copy code

`GET /maps`


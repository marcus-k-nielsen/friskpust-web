@@ -1,2 +1,123 @@
# Frisk-Pust-Hjemmeside
Dette er hjemmesiden til vores frisk pust enhed
# Database to Flask Web Application

A small Python web application built with **Flask** that retrieves data from a database and displays it through a web interface.

The project was created to practice connecting a database to a Flask application and separating database logic from the web application itself.

## Overview

The application follows a simple data flow:

```text
Database
   │
   ▼
Database Connection
   │
   ▼
Data Retrieval
   │
   ▼
Flask Application
   │
   ▼
HTML Templates
   │
   ▼
Web Browser
```

The project demonstrates how data can be retrieved from a database and made available through a Flask-based web application.

## Technologies

* **Python**
* **Flask**
* **HTML / Jinja2**
* **Database**
* **SQL**

## Project Structure

```text
DB-To-Flask-App/
│
├── templates/
│   └── ...
│
├── app.py
├── database_connections.py
├── get_data.py
├── README.md
└── .gitignore
```

### `app.py`

The main Flask application. It handles the web application and routes requests to the appropriate pages.

### `database_connections.py`

Contains the database connection logic used by the application.

### `get_data.py`

Handles retrieving data from the database for use by the Flask application.

### `templates/`

Contains the HTML/Jinja2 templates used to display the data in the browser.

## How It Works

The application separates the database functionality from the Flask application.

1. The application establishes a connection to the database.
2. Data is retrieved using Python.
3. Flask receives the retrieved data.
4. The data is passed to an HTML/Jinja2 template.
5. The template displays the data in the browser.

This provides a basic example of connecting a backend application to a database and presenting the stored information through a web interface.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/TezzePP/DB-To-Flask-App.git
cd DB-To-Flask-App
```

Install the required Python packages:

```bash
pip install flask
```

Configure the database connection in the application before starting the server.

Run the Flask application:

```bash
python app.py
```

The application can then be accessed through the local Flask server.

## What I Learned

This project gave me experience with:

* Connecting Python applications to databases
* Retrieving data using SQL
* Building Flask applications
* Using Jinja2 templates
* Separating database logic from application logic
* Passing backend data to a web interface

## Project Status

This is a small educational project focused on learning the fundamentals of database integration with Flask.

It is not intended to be a production-ready application.

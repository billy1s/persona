# Persona API

A basic flask restful API to a persona dataset

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```
Initialise database if starting fresh
```bash
flask db init
flask db migrate -m "first migrate"
flask db upgrade
```
To load data navigate to the admin page (/admin) and press the button "Ingest New Data"
This will ingest the zipped JSON data location in 
"persona\flaskr\api\inbound_data\files_to_process"
and load it into the database

## Front End

The API features a very basic frontend featuring a landing page, a search tab which lets you search for a user by username and an admin panel used to activate data ingestion.
## API routes

```bash
- GET /api/search/{username} - Searches for a user by username
- GET /api/people - Returns all users with pagination
- DELETE /api/people/{username} - Deletes user by username
```
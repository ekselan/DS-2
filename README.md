# DS

## Resources
- Postgres Database
- Flask
- Heroku  

## Installation Instructions for Dependencies (pipenv, Mac/Linux)

- Flask, Flask-Cors, Psycopg2, Gunicorn, Requests, Dotenv
```sh
pipenv install Flask flask-cors psycopg2-binary gunicorn requests python-dotenv
```
- PostgreSQL Database Connection
Example of format to place credentials inside a .env file:
```py
DB_USER="___________"
DB_NAME="___________"
DB_PASSWORD="___________"
DB_HOST="___________"
```

---

## Running the app locally using Flask  
**In a terminal:**  
Mac/Linux:  
`FLASK_APP=MedCab flask run`  
Windows:  
`export FLASK_APP=MedCab` (set env var)  
`flask run`

## Heroku App: https://med-cab-1415.herokuapp.com/

Endpoints if deployed to Heroku:  
Below are the routes that return key-value pair data in JSON from a postgreSQL database. 
```sh
https://med-cab-1415.herokuapp.com/
https://med-cab-1415.herokuapp.com/strains
https://med-cab-1415.herokuapp.com/recx
https://med-cab-1415.herokuapp.com/model
```

## Heroku App II: https://greensolx2.herokuapp.com/

Endpoints if deployed to Heroku:  
Below are the routes that return key-value pair data in JSON from a postgreSQL database. 
```sh
https://greensolx2.herokuapp.com/
https://greensolx2.herokuapp.com/strains
https://greensolx2.herokuapp.com/recx
```

## Heroku Deployment
- Add "Procfile" (case-sensitive) with following content:
```sh
web: gunicorn "MedCab:create_app()"
```
- Log in to Heroku from the CLI (first time only):
```sh
heroku login
```
- Creating a new application server (MUST BE DONE FROM WITHIN THE REPOSITORY'S ROOT DIRECTORY):
```sh
git remote -v
heroku create # optionally provide a name... "heroku create my-app-name"
git remote -v
```
- Deploying to Production:
```sh
git push heroku master
```
- Viewing production app in browser:
```sh
heroku open
```
- Checking production server logs:
```sh
heroku logs --tail
```
- Configuring production environment variables:
```sh
heroku config:set DB_USER="___________"
heroku config:set DB_NAME="___________"
heroku config:set DB_PASSWORD="___________"
heroku config:set DB_HOST="___________"
```

# DS
Data Science repository for BW-Med-Cab-2. Includes API calls and interaction instructions. Also includes steps to re-create API locally, including dependency installations.

---

## Heroku App: https://med-cab-1415.herokuapp.com/

Endpoints if deployed to Heroku:  
Below are the routes that return key-value pair data in JSON from a postgreSQL database. 
```sh
https://med-cab-1415.herokuapp.com/
https://med-cab-1415.herokuapp.com/strains
https://med-cab-1415.herokuapp.com/recx
https://med-cab-1415.herokuapp.com/model
https://med-cab-1415.herokuapp.com/model/<symptoms_string>
https://med-cab-1415.herokuapp.com/data
https://med-cab-1415.herokuapp.com/toptenrating
https://med-cab-1415.herokuapp.com/toptenflavor
```

## Heroku App II: https://greensolx2.herokuapp.com/

Endpoints if deployed to Heroku:  
Below are the routes that return key-value pair data in JSON from a postgreSQL database. 
```sh
https://greensolx2.herokuapp.com/
https://greensolx2.herokuapp.com/strains
https://greensolx2.herokuapp.com/recx
https://greensolx2.herokuapp.com/model
https://greensolx2.herokuapp.com/model/<symptoms_string>
https://greensolx2.herokuapp.com/data
https://greensolx2.herokuapp.com/toptenrating
https://greensolx2.herokuapp.com/toptenflavor
```

*Note on dual APIs:* Both APIs provide same functionality, use same model, and can be used interchangeably. Presence of both is for development and production workflow, as well as back up API.

---

## Heroku API
- **Strain Recommender Tool**
    - **To get strain recommendations**, type/insert a "symptoms string" into:
        - https://med-cab-1415.herokuapp.com/model/<symptoms_string> 
        - or: 
        - https://greensolx2.herokuapp.com/model/<symptoms_string>
        - **Replace <symptoms_string> with ailments/symptoms**
    - **Examples:**
        - ***Single Entry:***
        ```
        https://med-cab-1415.herokuapp.com/model/insomnia
        ```
        - ***Two Inputs:*** (can type in commas and spaces)
        ```
        https://med-cab-1415.herokuapp.com/model/insomnia, anxiety
        ```
        - ***Multi-Input:***
        ```
        https://med-cab-1415.herokuapp.com/model/insomnia, anxiety, fatigue, spasms, muscle pain
        ```
    - **Output** (json key value pairs)
        - ***Schema:*** 
        ```
        --strain        (strain name, string)
        --id            (strain id, string)
        --flavors       (flavors, string)
        --effects       (positive effects, string)
        --medical       (medical effects, string)
        --type          (indica, hybrid or sativa, string)
        --rating        (up to 5 stars, float)
        ```
        - ***Example:***
        ```
        {"strain":"Crystal Gayle","id":634,"flavors":"Earthy, Diesel, Skunk","effects":"Hungry, Euphoric, Happy, Creative, Focused","medical":"Muscle Spasms","type":"hybrid","rating":4.4}
        ```
- **Routes for data grabs / queries:**
    - ***View all strains in database***
    ```
    https://med-cab-1415.herokuapp.com/strains
    ```
        - Returns strain id, name, and rating
    - ***View all data in database***
    ```
    https://med-cab-1415.herokuapp.com/data
    ```
        - Returns strain name, id, flavors, effects, medical, type, rating, flavor
    - ***View top ten highest rated strains***
    ```
    https://med-cab-1415.herokuapp.com/toptenrating
    ```
        - Returns strain names, sorted in descending order, filtered by star rating and length of "medical" description
    - ***View top ten "most flavorful" strains***
    ```
    https://med-cab-1415.herokuapp.com/toptenflavor
    ```
        - Returns strain names, sorted in descending order, filtered by length of "flavors" description
---

## Resources
- Postgres Database
- Flask
- Heroku  

---

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

---

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
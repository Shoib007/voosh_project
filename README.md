**User Login/Register with Social Oauth2**

Install [Python](https://www.python.org/downloads/)

Step 1:
Clone the repo

    git clone https://github.com/Shoib007/voosh_project.git
    cd voosh_project

Step 2:
Install dependencies

    pip install -r requirement.txt

Step 3:
Migrate the model to sqlite db

    python manage.py makemigrations
    python manage.py migrate

Step 4:
Run the server

    python manage.py runserver

API Documentation


| END POINT | METHOD | PAYLOAD  | Authentication |
|--|--|--|--|
| api/token/ | post | username, password | No |
| api/token/refresh/ | post | refresh_token| Yes |
| users/ | get, post| post-> username, password, email | Yes|
| users/{id} | get, patch| {userinfo for update} | Yes |
| logout/ | post | refresh_token | Yes |
| swagger/ | get| Swagger API Doc | No |
| auth/convert-token | post| client_id, client_secret, token, backend, grant_type | Yes|


> Note: **auth/convert-token** api is for social authentication like Google, Facebook, GitHub, etc.
> Follow [drf-social-oauth2](https://drf-social-oauth2.readthedocs.io/en/latest/integration.html) documentation for more details








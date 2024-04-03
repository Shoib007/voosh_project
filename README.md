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



**Facebook Login**
Test the api using the following command

    curl  -X  POST  -d  "grant_type=convert_token&client_id=<client_id>&client_secret=<client_secret>&backend=facebook&token=<facebook_token>"  http://localhost:8000/auth/convert-token

You can obtain the ID (SOCIAL_AUTH_FACEBOOK_KEY) and secret (SOCIAL_AUTH_FACEBOOK_SECRET) of your app from [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/).

**Google Login**
Test the API using the following command

    curl  -X  POST  -d  "grant_type=convert_token&client_id=<django-oauth-generated-client_id>&client_secret=<django-oauth-generated-client_secret>&backend=google-oauth2&token=<google_token>"  http://localhost:8000/auth/convert-token

To obtain your app’s ID (SOCIAL_AUTH_GOOGLE_OAUTH2_KEY) and secret (SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET), visit [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials). For more details on how to create an ID and secret, visit [https://developers.google.com/identity/protocols/OAuth2](https://developers.google.com/identity/protocols/OAuth2).


**GitHub Login**
Test the API by following the steps

 1. As described by GitHub’s [documentation](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps), you need to follow a few steps in order to generate the access token to post requests on behalf of a user, team or organisation. The first step, your application will need to Request a user’s GitHub identity by sending a GET request to

   

     https://github.com/login/oauth/authorize

The only compulsory parameters are client_id=<the app client id> and redirect_uri=<the redirect you added in your app>. You will be redirected to a new location in your browser, such as [http://example.com/complete/github?code=d9ba2b356d27455970bf](http://example.com/complete/github?code=d9ba2b356d27455970bf), copy the code=value from it. Remember, this is only value for 10 minutes. This process should be automated by the module/library integrated into your front-end application.
2. The second step is to send a request to:

    curl  -X  POST  -d  "client_id=<client id>&client_secret=<client secret>&code=<code from previous step>&redirect_uri=<your redirect uri>"  https://github.com/login/oauth/access_token
You should receive an access token from the previous step. Once you have the access token, test your configuration
3. To test the configuration settings, execute the following command:

    curl  -X  POST  -d  "grant_type=convert_token&client_id=<django-oauth-generated-client_id>&client_secret=<django-oauth-generated-client_secret>&backend=github&token=<github_token>"  http://localhost:8000/auth/convert-token

Read more about GitHub’s configuration at [Python Social Auth - Github Page](https://python-social-auth.readthedocs.io/en/latest/backends/github.html)


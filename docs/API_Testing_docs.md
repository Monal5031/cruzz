# Document contain the procedure how the API url were initially tested.

:: Note :: Before testing any of the following urls make sure you have a local DB setup, server running and postman installed.

Use the given URL as Postman's target URL.

### Login API
1. Registration API

Method: POST

Auth type: Basic Auth

URL:
```
    http://127.0.0.1:8000/api/authentication/users/registration
```

Body:
```json
{
  "user": {
    "email": "test_email_here",
    "username": "test_username_here",
    "password": "test_password_here"
  }
}
```


2. Login API

Method: POST

Auth type: Basic Auth

URL:
```
    http://127.0.0.1:8000/api/authentication/users/login
```

Body:
```json
{
  "user": {
    "email": "test_email_here",
    "username": "test_username_here",
    "password": "test_password_here"
  }
}
```
or alternatively, use Bearer Token Auth and send the Token in header as in point 3.


3. Update user data API.

Method: GET

Auth Type: Bearer Token

URL:
```
    http://127.0.0.1:8000/api/authentication/users/update/
```

Method: GET

Header:

| Key                | Value                   |
|:------------------:|:-----------------------:|
| Content-Type       | application/json        |
| Authorization      | Token token_value_here  |

Method: POST

Auth Type: Bearer Token

Header:

| Key                | Value                   |
|:------------------:|:-----------------------:|
| Content-Type       | application/json        |
| Authorization      | Token token_value_here  |

Body:

```
{
  "user": {
  	"username": "peace",
  	"email": "mohit@yadav.com",
  	"first_name": "mohit"
  }
}
```

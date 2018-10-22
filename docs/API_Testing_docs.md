# Document contain the procedure how the API url were initially tested.

:: Note :: Before testing any of the following urls make sure you have a local DB setup, server running and postman installed.

Use the given URL as Postman's target URL.

### Login API
1. Registration API

    URL:
    ```
        <server_url>/api/authentication/users/registration
    ```

    Method: POST
    
    Auth type: Basic Auth
    
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
    
    URL:
    ```
        <server_url>/api/authentication/users/login
    ```
    
    Method: POST
    
    Auth type: Basic Auth
    
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

    URL:
    ```
        <server_url>/api/authentication/users/update/
    ```
        
    -
        Method: GET
        
        Auth Type: Bearer Token
        
        Header:
        
        | Key                | Value                   |
        |:------------------:|:-----------------------:|
        | Content-Type       | application/json        |
        | Authorization      | Token token_value_here  |
    
    - 
        Method: POST
        
        Auth Type: Bearer Token
        
        Header:
        
        | Key                | Value                   |
        |:------------------:|:-----------------------:|
        | Content-Type       | application/json        |
        | Authorization      | Token token_value_here  |
        
        Body:
        ```json
        {
          "user": {
            "username": "username_here",
            "email": "email_here",
            "first_name": "first_name_here"
          }
        }
        ```

4. Retrieve Profile of registered user.

    URL:
    ```
        <server_url>/api/profile/retrieve/<username>/
    ```
    
    Method: GET
    
    Auth Type: Bearer Token
    
    Header:
    
    | Key                | Value                   |
    |:------------------:|:-----------------------:|
    | Content-Type       | application/json        |
    | Authorization      | Token token_value_here  |
        
    
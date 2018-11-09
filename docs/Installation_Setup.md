Installation setup:

Initial setup:

1. Install python
    ```bash
       sudo apt-get install python3.6
    ```

2. Fork and then clone repo
    ```bash
       git clone <forked-repo-link>.git
    ```

3. Install virtual environment
    ```bash
       sudo apt-get install virtualenv
    ```

4. Create py3.6 virtualenv
    ```bash
       virtualenv -p python3.6 venv
    ```

5. Install requirements
    ```bash
       pip install requirements.txt 
    ```
    
    before using installing requirements make sure your pip is upto date
    ```bash
       pip install --upgrade pip
    ```

Project Databse setup:
1. Install psql (PostgreSQL) 9.5.12

2. Login to postgres
    ```bash
       sudo su - postgres
    ```
    It will ask for your root password.

3. Login to psql
    ```bash
       psql
    ```
    It will ask for your psql password.

4. Create database
    ```bash
       create database cruzz;
    ```

5. Create DB user
    ```bash
       create user cruzz with password 'cruzz12345';
    ```

6. Grant permissions to user
    ```bash
       grant all on database cruzz to cruzz;
    ```


Migrate database and runserver

:Note: Migration files are already included in the repo so no need to create migrations.

1. First activate virtualenv
    ```bash
       source venv/bin/activate
    ```

2. Migrate database
    ```bash
       python manage.py migrate
    ```

3. Runserver
    ```bash
       python manage.py runserver
    ```


To test things out, go through the URL endpoints in [APT_Testing_docs](API_Docs.md).

You can use `Postman` or similar services for testing endpoints.

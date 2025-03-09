# Dialflo-Backend-Task

###  Features

- **Support Agent**: API which takes query and username, phone (optional) as payload and return the response Order stauts.



## Setup Instructions

### Clone the Repository

To get started, clone the repository to your local machine:

```sh
git clone https://github.com/Faizgeeky/Dialflo-backend
cd Dialflo-backend
```

### Setting Up the .env change and put db creds

```
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_NAME = 'dialflo'
```


### Setting Up the Rest API's


1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```


###   🚀🚀 Ready to launch your API Endpoints

2. Run uvicorn server:
    ```sh
    uvicorn api.main:app --reload 
    ```

###   🚀🚀 Test all API's using pytest

3. Run API testing :
    ```sh
    pytest 
    ```

   
### API's Documentation

An enpoint http://localhost:8000/docs will have list of schema and api endpoints. Swagger OpenAPI Document

     

### API Documentations 

- It can be downloaded and test live while running the api's on webbrowser 

    <!-- API Testing -->
    http://127.0.0.0:8000/docs 

    <!-- API Documentation -->
    http://127.0.0.0:8000/redoc

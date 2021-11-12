# Squirro
Project for interview at Squirro


## Run
To run this project:

1. Create .env file from .env.template and complete it

2. ```docker-compose build```

    ```docker-compose up```


## Endpoints

1. "/doc"
   1. method: POST
   2. Content-Type: 'x-www-form-urlencoded'
   3. param: 'text' -> text to store
2. "/doc/<int:pk>"
   1. method: GET
   2. Content-Type: 'application-json'
   3. param: 'document_id' -> id of document

# sde-project
GraphQL vs REST framework

# system Requirements 

Python 3.8

#Libraries
Flask
SQL-Alchamey
Ariadne
Pandas



# how to run the application

1. Go to GraphQL-app folder
2. Install all dependencies 
3. Run flask shell and type command db.create_all() to initialise the database
4. Run flask run --port=5000 to run the application
5. To query the application open the url http://127.0.0.1/graphql to run any graphic based query


# how to run load test
1. Open shell
3. Run pip install locust
4. Run locust -f locustfile.py
5. Open the url http://127.0.0.1:8089 

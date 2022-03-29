# Online Movie Store
The project is a simple paradigm of a online video club and it is implemented using Django REST framework.

Below is a Conceptual Model which illustrates all the classes involved in our example :

![This is an image](https://drive.google.com/uc?export=view&id=1i9_1Piphdb6QKqt3cZXAoKhuT1Sjb8S9)

where :
- **Category** : is a category of a movie (e.g. Fantasy, Comedy)
- **User** : is a user who registers on the platform. Each registered user is certified with a token.
- **Movie** : is a movie that the user can rent. For simplicity, we assume that each movie can be rented by only one user when it is available.
- **Rental** : contains all rentals made by users.

## Functionalities
Each **registered** user can do the following:
- See all available movies based on given category or query
- See details for a specific movie
- Rent a movie
- Pay / Return a movie

## Set Up
Assuming you have the docker-compose installed,in order to run the api follow the steps below:

1. Go to the project directory and execute the following statement in the cmd:

```
docker-compose up --build
```

2. Executing the above command, the next three containers are created :
* **Postgres** : postgres database (port: 5432)
* **Pgadmin4** : web-based GUI tool for postgres (port: 5050)
* **Redis**    : cache (port: 6379)
* **App** (port: 8000)

##  Testing
Τo test the api you can:
1. run manual tests by registering some users and then perform the above functionalities using the given postman collection
2. run the automated tests by running 
```
python manage.py test 
```

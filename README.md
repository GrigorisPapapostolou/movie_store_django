# Online Movie Store
The project is a simple paradigm of a online video club and it is implemented using Django REST framework.

Below is a Conceptual Model which illustrates all the classes involved in our example :

![This is an image](https://drive.google.com/uc?export=view&id=1i9_1Piphdb6QKqt3cZXAoKhuT1Sjb8S9)

where :
- **Category** : category of a movie (e.g. Fantasy, Comedy)
- **User** :  user who registers on the platform. Each registered user is certified using a token.
- **Movie** : movie that a user can rent. (Note: For simplicity, we assume that each movie has one copy)
- **Rental** : contains all rentals made by users.

## Functionalities
Each **registered** user can :
- See all available movies based on given category / query
- See details for a specific movie
- Rent a movie
- Return and return a movie

## Set Up
It is required to have installed the docker-compose and a clone of the project in order to test the api:

1. Go to the project directory and execute the following statement in the cmd:

```
docker-compose up --build
```
Executing the above command, the next three containers are created :
* **App**      : movie store api (port: 8000)
* **Postgres** : postgres database (port: 5432)
* **Pgadmin4** : GUI tool for postgres (port: 5050)
* **Redis**    : cache (port: 6379)
* **Celery**   


##  Testing
Τo test the api you can:
1. run manual tests by registering some users and then perform the above functionalities using the given postman collection
2. run the automated tests by running 
```
python manage.py test 
```
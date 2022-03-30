# Online Movie Store
The project is a simple paradigm of a online video club and it is implemented using Django REST framework.

Below is a conceptual model which illustrates all the classes involved in our example :

<img width="296" alt="UML_diagram" src="https://user-images.githubusercontent.com/20031140/160915598-faa25a51-f456-4f61-9caa-d376a6048510.png">

where :
- **Category** : category of a movie 
- **User** :  user who registers on the platform. Each registered user is certified using a token.
- **Movie** : movie that a user can rent. (**Note**: we assume that each movie has one copy)
- **Rental** : contains all rentals made by users.

## API Functionalities
Each **registered** user can :
- See all available movies based on given category / query
- See details for a specific movie
- Rent a movie
- Return and pay a movie

## Set Up
Requirements : 
- docker-compose 
- copy of the repository


 Go to the project directory and execute the following command:

```
docker-compose up --build
```
By executing the mentioned command, the below architecture is created: 

<img width="763" alt="architecture" src="https://user-images.githubusercontent.com/20031140/160917987-97852d4a-8752-4a3f-bff6-19a5a3de3a38.png">

- **Celery** is an asynchronous **task queue** based on distributed message passing. Message passing model allows multiple processes to read and write data to the message queue without being connected to each other. It also is focused on real-time operation, but supports scheduling as well. In our example we defined the amount of money the user has to pay as celery task. 
- **Redis** is a performant, in memory, key-value data store. It is used to store messages produced by the application code describing the work to be done in the Celery task queue. Redis also serves as storage of results coming off the celery queues which are then retrieved by consumers of the queue. In our case we use it to save the details of a movie recently requested by a user.
- **Postgres** is a object-relational database system provides reliability and data integrity.
- **PgAdmin** is a web-based GUI tool used to interact with the Postgres database sessions, both locally and remote servers as well. You can use PGAdmin to perform any sort of database administration required for a Postgres database.

##  Testing
- **Manual Testing**: run manual tests by registering some users and then perform the above functionalities using the given postman collection
- **Interactive Testing**: connect to the container that runs the application (**docker exec -it container_id bash**) and then run the following command
```
python manage.py test 
```
- **Automated Testing**: use GitHub Actions which is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. I create a workflow at **.github\workflows** that test every pull request to the master branch and every push on develop branch.


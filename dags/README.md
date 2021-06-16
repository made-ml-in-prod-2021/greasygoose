## **HW3 launching hints**

cd dags/images/airflow-ml-base

(or cd images/airflow-ml-base)

docker build . -t airflow-ml-base:latest

cd ../..

docker-compose up --build

listen on

http://localhost:8080/  => http://localhost:8080/

Like in .yaml file:

username: admin
password: admin 

docker-compose down

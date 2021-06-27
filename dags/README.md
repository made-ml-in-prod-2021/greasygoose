## **HW3 launching hints**

cd dags/images/airflow-ml-base

(or cd images/airflow-ml-base)

docker build . -t airflow-ml-base:latest

cd ../..

docker-compose up --build

Listening at: http://0.0.0.0:8080 (26)

  => http://localhost:8080/

Like in .yaml file:

username: admin
password: admin 

docker-compose down

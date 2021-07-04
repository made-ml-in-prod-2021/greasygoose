## **HW3 launching hints**

In terminal go to:

cd images/airflow-ml-base

(or cd dags/images/airflow-ml-base)

docker build . -t airflow-ml-base:latest

cd ../..

docker-compose up --build

Listening at: http://0.0.0.0:8080 (26)

  => http://localhost:8080/
(Open in browser)

(Note: if airflow fails to start due to MSSQL error or internal errors, Press Ctrl+C, then compose up --build (w/o -compose down!!!). It will run some upgrades and start)

Like in .yaml file enter:

username: admin
password: admin 


To shutdown:

docker-compose down

List of running dags:

![Alt text](imgs/DAG_list.png?raw=true "List_of_running_dags")


Generate data DAG graph and tree:

![Alt text](imgs/DAG1_graph.png?raw=true "DAG1_graph")
![Alt text](imgs/DAG1_tree.png?raw=true "DAG1_tree")


Train model DAG graph and tree:

![Alt text](imgs/DAG2_graph.png?raw=true "DAG2_graph")
![Alt text](imgs/DAG2_tree.png?raw=true "DAG2_tree")


Apply model DAG graph and tree:

![Alt text](imgs/DAG3_graph.png?raw=true "DAG3_graph")
![Alt text](imgs/DAG3_tree.png?raw=true "DAG3_tree")
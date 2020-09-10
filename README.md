# Spark_Airflow_Hive_Docker
Run ETL by Spark, Airflow, Hive on Docker Desktop

Deploy Application
1. Run Docker Desktop
2. Open Terminal
3. $ git clone https://github.com/autthapone/Spark_Airflow_Hive_Docker.git
4. $ cd Spark_Airflow_Hive_Docker/app
5. $ docker-compose build
6. $ docker-compose up

Re-Deploy Application
1. Exit Docker-compose process
2. $ docker-compose down
3. Coding
4. $ cd Spark_Airflow_Hive_Docker/app
5. $ git add .
6. $ git status
7. $ git commit -m "Deploy message"
8. $ git push origin master
9. $ docker-compose build
10. $ docker-compose up

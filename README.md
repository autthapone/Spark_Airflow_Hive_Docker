# Spark_Airflow_Hive_Docker
Run ETL by Spark, Airflow, Hive on Docker Desktop (Windows)

Deploy Application
1. Run Docker Desktosp
2. Open Terminal
3. $ git clone git@github.com:autthapone/Spark_Airflow_Hive_Docker.git
4. $ cd /Spark_Airflow_Hive_Docker/app
5. $ docker-compose build
6. $ docker-compose up

Re-Deploy Application
1. Run Docker Desktop
2. Open Terminal
3. Exit Docker-compose process
4. $ docker-compose down
5. Coding
6. $ cd /Spark_Airflow_Hive_Docker/app
7. $ git add .
8. $ git status
9. $ git commit -m "Deploy message"
10. $ git push origin master
11. $ docker-compose build
12. $ docker-compose up

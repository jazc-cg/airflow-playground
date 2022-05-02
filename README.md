# Airflow-PlayGround

This project is to learn about Airflow and its components locally.

This is ***not*** intended for production usage. 

So, please ***do not*** clone this repo, you can download it as zip and unzip on your local machine.

#

### What you can do: 
1. You can create your own dag and test your code or logic
2. You can easily upgrade the airflow version by simply changing the version in the docker-compose.yaml (line 4).

### Start and Stop:
You can either do `docker-compose up -d --build` on the terminal or you can run `start-airflow.sh`.

To stop, you can run `docker-compose down` or `stop-airflow.sh`.

### Services:

* airflow-scheduler - The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.

* airflow-webserver - The webserver is available at http://localhost:8080.

* airflow-init - The initialization service.

* postgres - The database.

### Configuration and Setup:

* Basic Airflow cluster configuration for LocalExecutor with PostgreSQL. This configuration is for local development only.

* If you don't want to load the sample dag jobs, you change AIRFLOW__CORE__LOAD_EXAMPLES to false


#

AIRFLOW_IMAGE_NAME           - Docker image name used to run Airflow.
                               Default: apache/airflow:2.2.5

_AIRFLOW_WWW_USER_USERNAME   - Username for the administrator account (if requested).
                               Default: airflow

_AIRFLOW_WWW_USER_PASSWORD   - Password for the administrator account (if requested).
                               Default: airflow

#

### Feel free to modify this file to suit your needs.

* Reference: https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html
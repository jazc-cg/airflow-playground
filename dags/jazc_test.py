from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from customized.operators.bash_operator import MyBashOperator

default_args = {
    'owner': 'jazc',
    'depends_on_past': False,
    'email': ['jae.choi@capgroup.com'],
}


with DAG(
    dag_id = "jazc_test_dag",
    default_args = default_args,
    catchup = False,
    schedule_interval = None,
    start_date = datetime.today(),
    tags=['test_jazc']
) as dag:
    @task(task_id="hello_world")
    def say_hello():
        print("Hello World")
        return "Hello"
        
    @task(task_id="bye_world")
    def bye_world():
        print("Bye World")
        return ("Bye")

    @task(task_id="hello_bye_world")
    def hello_bye(a, b):
        print(a, b)

    my_custom_operator = MyBashOperator(
        task_id='custom_bash', 
        command="echo Hellow"
    )


    hello_bye(say_hello, bye_world) >> my_custom_operator

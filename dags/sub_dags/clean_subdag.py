from airflow.models import DAG
from airflow.operators.dummy import DummyOperator

def clean_subdag_factory(parent_dag_id, parent_task_id, default_args):
    with DAG(
        f"{parent_dag_id}.{parent_task_id}", 
        default_args=default_args
    ) as dag:
        clean_a = DummyOperator(task_id='clean_a')
        clean_b = DummyOperator(task_id='clean_b')
        clean_c = DummyOperator(task_id='clean_c')
    return dag

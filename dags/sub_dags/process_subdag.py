from airflow.models import DAG
from airflow.operators.dummy import DummyOperator

def process_subdag_factory(parent_dag_id, parent_task_id, default_args):
    with DAG(
        f"{parent_dag_id}.{parent_task_id}", 
        default_args=default_args
    ) as dag:
        process_a = DummyOperator(task_id='process_a')
        process_b = DummyOperator(task_id='process_b')
        process_c = DummyOperator(task_id='process_c')
    return dag

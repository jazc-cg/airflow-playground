from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.helpers import chain

from airflow.operators.subdag import SubDagOperator

from sub_dags.clean_subdag import clean_subdag_factory
from sub_dags.process_subdag import process_subdag_factory


from datetime import datetime

default_args = {
    'start_date': datetime(2022,5,11)
}

with DAG(
    'subdag', 
    schedule_interval="@daily", 
    catchup=False,
    default_args=default_args) as dag:

    extract = DummyOperator(task_id='reach_api')
    
    # clean_a = DummyOperator(task_id='clean_a')
    # clean_b = DummyOperator(task_id='clean_b')
    # clean_c = DummyOperator(task_id='clean_c')
    
    # process_a = DummyOperator(task_id='process_a')
    # process_b = DummyOperator(task_id='process_b')
    # process_c = DummyOperator(task_id='process_c')

    clean_task = SubDagOperator(
        task_id='clean_task_dag',
        subdag=clean_subdag_factory(
            parent_dag_id='subdag',
            parent_task_id='clean_task_dag',
            default_args=default_args
        )
    )

    process_task = SubDagOperator(
        task_id='process_task_dag',
        subdag=process_subdag_factory(
            parent_dag_id='subdag',
            parent_task_id='process_task_dag',
            default_args=default_args
        )
    )
    
    store = DummyOperator(task_id='store')

    
    # chain(extract, [clean_a, clean_b, clean_c], [process_a, process_b, process_c], store)
    chain(extract, clean_task, process_task, store)
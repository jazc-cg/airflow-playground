from dag_configs.dagfactory import DagFactory


config_file = "/opt/airflow/dags/dags_yaml/dynamic_dag_factory_ex1.yml"
dag_factory = DagFactory(config_file)

# Creating task dependencies
dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())

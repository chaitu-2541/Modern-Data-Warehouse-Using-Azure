
from airflow.providers.microsoft.azure.operators.data_factory import AzureDataFactoryRunPipelineOperator
from airflow.decorators import dag, task
from datetime import datetime ,timedelta
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator

default_args = {
    "owner": "fahmy",
    "retries": 0,
    "retry_delay": timedelta(minutes=1)
}

# Define the basic parameters of the DAG, like schedule and start_date
@dag(
    start_date=datetime(2024, 1, 1),
    dag_id="trigger_sales_dwh_pipeline",
    schedule="@daily",
    catchup=False,
    default_args = default_args,
    tags=["Trigger-DWH"]
)
def sales_dwh():
    azure_data_factory = AzureDataFactoryRunPipelineOperator(
        task_id="run_azure_data_factory_pipeline",
        pipeline_name="get data from source",
        resource_group_name="Sales-DWH",
        factory_name="salesdwh",
        azure_data_factory_conn_id="ADF_conn"
    )
    run_databricks_job = DatabricksRunNowOperator(
    task_id='run_databricks_job',
    databricks_conn_id='db_conn',  
    job_id='264642803282902'
    )
        azure_data_factory>>run_databricks_job
sales_dwh()

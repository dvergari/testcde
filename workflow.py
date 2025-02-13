from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils import timezone
from datetime import timedelta
from dateutil import parser
from getdata.download import download
from uploads3.uploadS3 import uploadS3

dag = DAG(
    dag_id='Load to Iceberg',
    schedule_interval=None,
    is_paused_upon_creation=False,
    default_args={
        'owner': 'dvergari',
        'email_on_failure': True,
        'email': ['dvergari@cloudera.com', ''],
    },

download_first_file = PythonOperator(
    dag=dag,
    task_id='Download first file',
    python_callable=download,
    params={"url": "https://drive.google.com/uc?id=1N1xoxgcw2K3d-49tlchXAWw4wuxLj7EV&export=download", "filename": "customers.csv"}
)

)
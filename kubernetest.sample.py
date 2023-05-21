from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='kubernetes_sample', default_args=args,
    schedule_interval=None,
    start_date=days_ago(2),
    tags=['example'],
) as dag:

    start_task = KubernetesPodOperator(
        task_id="run_sample_pod",
        name="run_sample_pod",
        namespace='default',
        in_cluster=True,
        is_delete_operator_pod=True,
    )

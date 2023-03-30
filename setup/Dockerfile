FROM apache/airflow:2.2.3-python3.9

RUN pip install --user 'apache-airflow[kubernetes,celery,postgres,ssh,kafka]'
RUN pip install --user GitPython
RUN pip install --user kafka-python
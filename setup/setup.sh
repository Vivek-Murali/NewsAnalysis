#!/bin/sh
AIRFLOW__CORE__FERNET_KEY=$(python ./fernet.py)
echo "$AIRFLOW__CORE__FERNET_KEY"
docker build -t sharpnel/arckafkaairflow:v1.0.0 .
docker push sharpnel/arckafkaairflow:v1.0.0
echo "Docker Build Completed"
from cryptography.fernet import Fernet
import base64
import os
import logging


# Generate a Fernet key
fernet_key = Fernet.generate_key()

# Encode the key as a base64 string
encoded_key = base64.b64encode(fernet_key).decode()

# Setting the Environment Variable
os.environ['AIRFLOW__CORE__FERNET_KEY'] = encoded_key
os.putenv("AIRFLOW__CORE__FERNET_KEY", encoded_key)
print(encoded_key)

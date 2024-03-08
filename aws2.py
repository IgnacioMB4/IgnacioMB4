import os
import boto3


#pip install awscli
#aws configure
#AWS_ACCESS_KEY_ID = "AKIA4MTWH243ELQQNT4P"
#AWS_SECRET_ACCESS_KEY = "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"
#region = eu-north-1
#format = .png
#$env:AWS_ACCESS_KEY_ID="AKIA4MTWH243ELQQNT4P"
#$env:AWS_SECRET_ACCESS_KEY="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"

# Accede a las variables de entorno para obtener las credenciales
#AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Verifica si las credenciales están presentes
#if AWS_ACCESS_KEY_ID is None or AWS_SECRET_ACCESS_KEY is None:
#    raise ValueError("No se han proporcionado las credenciales de AWS")

# Crea el cliente de S3 utilizando las credenciales de entorno
#client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Crea un cliente de AWS S3 utilizando el perfil 'default'
client = boto3.Session(profile_name='default').client('s3')

# Sube el archivo a S3
client.upload_file('imagen2.jpg', 'clivi-infinite', 'prueba.jpg')

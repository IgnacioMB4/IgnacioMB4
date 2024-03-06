import boto3

AWS_ACCESS_KEY_ID = "AKIA4MTWH243ELQQNT4P"
AWS_SECRET_ACCESS_KEY = "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"

def upload(bucket_name, local_image_path):
    # Inicializar cliente de S3
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    # Nombre del archivo en S3 será el nombre del archivo local
    file_name = local_image_path.split('/')[-1]

    try:
        # Subir archivo a S3
        s3.upload_file(local_image_path, bucket_name, file_name)
        print("Imagen subida exitosamente a S3 en el bucket:", bucket_name)
    except Exception as e:
        print("Error al subir la imagen a S3:", str(e))

# Ejemplo de uso
bucket_name = 'clivi-infinite'  # Nombre de tu bucket
local_image_path = 'imagen2.jpg'  # Ruta local de la imagen que quieres subir
upload(bucket_name, local_image_path)

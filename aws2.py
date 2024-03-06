import boto3

AWS_ACCESS_KEY_ID = "AKIA4MTWH243ELQQNT4P"
AWS_SECRET_ACCESS_KEY = "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"

client = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

client.upload_file('imagen2.jpg', 'clivi-infinite', 'nano.jpg')

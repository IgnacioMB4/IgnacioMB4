from google.oauth2 import service_account
from googleapiclient.discovery import build
import io

# Función para subir la imagen a Google Drive y obtener la URL pública
def upload_image_to_drive(image_bytes, credentials_file, file_name):
    scopes = ['https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scopes)
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {'name': file_name}
    media = io.BytesIO(image_bytes)

    file = service.files().create(body=file_metadata, media_body=media, fields='webViewLink').execute()
    return file.get('webViewLink')
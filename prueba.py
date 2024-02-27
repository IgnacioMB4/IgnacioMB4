from google.cloud import storage

def subir_imagen_y_obtener_url(archivo_local, nombre_blob, nombre_bucket):
    # Inicializa el cliente de Google Cloud Storage
    cliente = storage.Client()

    # Obtén el bucket
    bucket = cliente.bucket(nombre_bucket)

    # Crea un nuevo blob en el bucket utilizando el nombre especificado
    blob = bucket.blob(nombre_blob)

    # Sube el archivo local al blob
    blob.upload_from_filename(archivo_local)

    # Genera la URL pública para acceder al archivo
    url = blob.public_url

    return url

if __name__ == "__main__":
    archivo_local = "ruta/a/tu/imagen.jpg"
    nombre_blob = "nombre_de_tu_imagen.jpg"
    nombre_bucket = "nombre_de_tu_bucket"

    url = subir_imagen_y_obtener_url(archivo_local, nombre_blob, nombre_bucket)
    print("URL de la imagen:", url)
from fastapi import APIRouter, File, UploadFile
import csv
import codecs


router = APIRouter()


@router.get(
    path="/",
    status_code=200,
    tags=["Home"],
    summary="Hola mundo de la aplicación",
    )
def Home():
    """
    # Hola mundo de la aplicación
    Este endpoint muestra un mensaje.

    Parámetros:
    - Request body:
        - Niguno
    - Request query:
        - Ninguno
    - Request header:
        - Ninguno
        
    - Request cookie:
        - Ninguno
    Regresa un JSON con el mensaje de bienvenida.
    """
    return {"message": "Bye World"}

@router.post(
    path="/upload",
    status_code=200,
    tags=["CSV"],
    summary="Procesa un archivo CSV y da una salida JSON",
    )
def upload(file: UploadFile = File(...)):
    """
    # Procesamiento de CSV
    Este endpoint devuelve un JSON con los parámetros agregados.

    Parámetros:
    - Request body:
        - File: Archivo .csv
    - Request query:
        - Ninguno
    - Request header:
        - Ninguno
        
    - Request cookie:
        - Ninguno
    Regresa un JSON con los datos agregados.
    """
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    data = {}
    for rows in csvReader:             
        key = rows['Index']  # Assuming a column named 'Index' to be the primary key
        data[key] = rows  
    
    file.file.close()
    return data

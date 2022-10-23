from fastapi import APIRouter, File, UploadFile
from scrapping.scrapper import scrap_inegi,scrap_maps,scrap_pyme_org
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
    for datum in data:
        data[datum].update({'Estrato':scrap_inegi(data[datum]['NombComp'][:-10])[0]})
        data[datum].update({'Registro':scrap_pyme_org(data[datum]['NombComp'][:-10], data[datum]['Estado'])})
        data[datum].update({'Reiews':scrap_maps(data[datum]['Direccion1']+
            data[datum]['Direccion2']+data[datum]['Direccion3']+data[datum]['Colonia']+data[datum]['CP'])})

    return data

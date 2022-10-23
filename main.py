from core import app

@app.get(
    path="/",
    status_code=200,
    tags=["default"],
    summary="Root",
    )
def hello_world():
    """
    # Hola mundo de la aplicación
    Este endpoint muestra un mensaje de bienvenida.

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
    return {"message": "Hello World"}


if __name__ == "__main__":
    app.run()
    # import uvicorn
    # import os
    
    # start = "main:app"
    # uvicorn.run(
    #     start, 
    #     # host="0.0.0.0", 
    #     port=80, 
    #     reload=True
    #     )
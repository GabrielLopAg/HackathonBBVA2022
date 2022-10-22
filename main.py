from core import app

if __name__ == "__main__":
    import uvicorn
    import os
    
    start = "main:app"
    uvicorn.run(
        start, 
        # host="0.0.0.0", 
        port=7000, 
        reload=True
        )
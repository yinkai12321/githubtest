import uvicorn
from main2 import app

if __name__ == "__main__":
    uvicorn.run(
        "main2:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
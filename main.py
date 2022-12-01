from os import environ

import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=environ.get('HOST', '127.0.0.1'),
        port=environ.get('PORT', '8000'),
        reload=True
    )

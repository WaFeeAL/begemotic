from os import environ

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from apps.hex.routes import hex_router
from apps.core.exception_handler import override_exception_handler
from apps.polygon.routes import polygon_router

app = FastAPI()
app.add_exception_handler(
    RequestValidationError, override_exception_handler
)

app.include_router(hex_router)
app.include_router(polygon_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=environ.get('HOST', '127.0.0.1'),
        port=environ.get('PORT', '8000'),
        reload=True
    )

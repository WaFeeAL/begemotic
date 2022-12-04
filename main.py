from os import environ

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from apps.begemotic.routes import router
from apps.core.exception_handler import override_exception_handler

app = FastAPI()
app.add_exception_handler(
    RequestValidationError, override_exception_handler
)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=environ.get('HOST', '127.0.0.1'),
        port=environ.get('PORT', '8000'),
        reload=True
    )

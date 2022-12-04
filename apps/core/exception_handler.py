from json import JSONDecodeError

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse


async def override_exception_handler(
        request: Request, exc: RequestValidationError
) -> JSONResponse:
    raw_errors = exc.raw_errors
    error_wrapper: ErrorWrapper = raw_errors[0]
    validation_error: ValidationError | JSONDecodeError = error_wrapper.exc
    if isinstance(validation_error, ValidationError):
        overwritten_errors = validation_error.errors()
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": jsonable_encoder(overwritten_errors)}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": validation_error.msg}
        )

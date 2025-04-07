from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status as drf_status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # DRF handled the exception
    if response is not None:
        custom_response = {
            "success": False,
            "status": response.status_code,
            "message": _get_error_message(response.data),
        }
        return Response(custom_response, status=response.status_code)

    # If DRF couldn't handle it (like a 500 error)
    return Response(
        {
            "success": False,
            "status": drf_status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Internal server error",
        },
        status=drf_status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def _get_error_message(data):
    if isinstance(data, dict):
        # Just return the first error message
        for key, value in data.items():
            if isinstance(value, list):
                return value[0]
            return str(value)
    return str(data)

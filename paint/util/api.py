from typing import Optional

from rest_framework.request import Request

from paint.types.api import QueryParamValue


def get_query_param(request: Request, param: str) -> Optional[QueryParamValue]:
    """Extracts the value for a given query param from the request
    
    Returns:
        the value of the param or else None
    """
    return request.query_params.get(param, None)
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.exceptions import NotFound
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse


def custom_exception_handler(exc, context):
    handlers = {
        'ValidationError': _handle_validation_error,
        'PermissionDenied': _handle_permission_denied_error,
        'NotAuthenticated': _handle_authentication_error,
        'MethodNotAllowed': _handle_method_not_allowed_error,
        'ThrottleError': _handle_throttle_error,
        'UnsupportedMediaType': _handle_unsupported_media_type_error,
        'ParseError': _handle_parse_error,
    }

    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response

def _handle_validation_error(exc, context, response):
    response_data = {
        'error': _('Validation Error'),
        'detail': _(str(exc)),
        'status_code':response.status_code
    }
    return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

def _handle_permission_denied_error(exc, context, response):
    response_data = {
        'error': _('Permission Denied'),
        'detail': _('You do not have permission to access this resource.'),
        'status_code':response.status_code
    }
    return Response(response_data, status=status.HTTP_403_FORBIDDEN)

def _handle_authentication_error(exc, context, response):
    response_data = {
        'error': _('Authentication Error'),
        'detail': _('Authentication is required to access this resource.'),
        'status_code':response.status_code
    }
    return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

def _handle_method_not_allowed_error(exc, context, response):
    response_data = {
        'error': _('Method Not Allowed'),
        'detail': _('The HTTP method used is not allowed for this resource.'),
        'status_code':response.status_code
    }
    return Response(response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def _handle_throttle_error(exc, context, response):
    response_data = {
        'error': _('Throttle Error'),
        'detail': _('Request rate limit exceeded. Please try again later.'),
        'status_code':response.status_code
    }
    return Response(response_data, status=status.HTTP_429_TOO_MANY_REQUESTS)

def _handle_unsupported_media_type_error(exc, context, response):
    response_data = {
        'error': _('Unsupported Media Type'),
        'detail': _('The request content type is not supported by this endpoint.'),
        'status_code':response.status_code
    }
    return Response(response_data, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

def _handle_parse_error(exc, context, response):
    response_data = {
        'error': _('Parse Error'),
        'detail': _('Unable to parse the request data.'),
        'status_code':response.status_code
    }
    return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


def _handle_not_found_error(request,exception):
    response_data = {
        'error': _('Not Found'),
        'detail': _('The requested url was not found'),
        'status_code':404
    }
    return JsonResponse(response_data)

def _handle_internal_server_error(request,exception):
    response_data = {
        'error':_('Bad Gateway'),
        'detail':_('Something went wrong...try again after sometimes'),
        'status_code':500
    }
    return JsonResponse(response_data)
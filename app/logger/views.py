"""
This file keeps views of logger module
"""
from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema,extend_schema_view,OpenApiParameter, OpenApiExample
import os

@extend_schema_view(
    get=extend_schema(
        description="""
        This is function is used to download the error.log file.
        Response will be a streaming response with .log extension
        """,

        tags=["Logger"],
        deprecated=False,
        summary="""Download error.log file""",
    )
)
class DownloadErrorLog(APIView):
    """
    This class downloads the error.log file 
    """
    def get(self, request):
        # Replace '/path/to/error.log' with the actual file path
        log_file_path = '/log/error.log'

        try:
            # Check if the file exists
            if os.path.exists(log_file_path):
                if os.path.getsize(log_file_path) == 0:
                    return Response(
                        {'detail': 'The log file is empty.'},
                        status=status.HTTP_200_OK
                    )
                def file_iterator(file_path, chunk_size=8192):
                    with open(file_path, 'rb') as f:
                        while True:
                            chunk = f.read(chunk_size)
                            if not chunk:
                                break
                            yield chunk

                response = StreamingHttpResponse(file_iterator(log_file_path))
                response['Content-Disposition'] = 'attachment; filename="error.log"'
                return response
            else:
                return Response(
                    {'detail': 'The log file does not exist.'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {'detail': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@extend_schema_view(
    get=extend_schema(
        description="""
        This is function is used to download the critical.log file.
        Response will be a streaming response with .log extension
        """,

        tags=["Logger"],
        deprecated=False,
        summary="""Download critical.log file""",
    )
)
class DownloadCriticalLog(APIView):
    """
    This class downloads the critical.log file 
    """
    def get(self, request):
        # Replace '/path/to/error.log' with the actual file path
        log_file_path = '/log/critical.log'

        try:
            # Check if the file exists
            if os.path.exists(log_file_path):
                if os.path.getsize(log_file_path) == 0:
                    return Response(
                        {'detail': 'The log file is empty.'},
                        status=status.HTTP_200_OK
                    )
                def file_iterator(file_path, chunk_size=8192):
                    with open(file_path, 'rb') as f:
                        while True:
                            chunk = f.read(chunk_size)
                            if not chunk:
                                break
                            yield chunk

                response = StreamingHttpResponse(file_iterator(log_file_path))
                response['Content-Disposition'] = 'attachment; filename="critical.log"'
                return response
            else:
                return Response(
                    {'detail': 'The log file does not exist.'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {'detail': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
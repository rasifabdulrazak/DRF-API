from rest_framework.views import APIView
from rest_framework.response import Response
from core.logger import error_log
from drf_spectacular.utils import extend_schema,extend_schema_view,OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .serializers import SampleSerializer



@extend_schema_view(
    get=extend_schema(
    description="""
    This is a custom view that does something awesome.
    """,
    parameters=[
        {
            "name": "param1",
            "in": "query",
            "type": "integer",
            "description": "A query parameter",
            "required": False,
        },
    ],

    tags=["User"],
    deprecated=False,
    summary="""Get Sample""",
    ),
    post=extend_schema(
    description="""
    This is a custom view that does something awesome.
    """,
    parameters=[
        {
            "name": "name",
            "in": "query",
            "type": "string",
            "description": "A query parameter",
            "required": True,
        },
        {
            "name": "place",
            "in": "query",
            "type": "string",
            "description": "A query parameter",
            "required": True,
        },
    ],
    tags=["User"],
    summary="""Post Sample""",
    )
    )
class SampleTest(APIView):
    serializer_class = SampleSerializer
    
    def get(self,request):
        error_log.error("wrongs")
        print(request.user)
        return Response({'test':'ok'})
    def post(self,request):
        return Response({'test':'ok'})
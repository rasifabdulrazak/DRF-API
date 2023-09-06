from rest_framework.views import APIView
from rest_framework.response import Response
from core.logger import error_log
from drf_spectacular.utils import extend_schema,extend_schema_view,OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes




@extend_schema_view(
    get=extend_schema(
    description="This is a custom view that does something awesome.",
    parameters=[
        {
            "name": "param1",
            "in": "query",
            "type": "integer",
            "description": "A query parameter",
            "required": False,
        },
    ],
    request={
        "content": {"application/json": {"schema": {"type": "object"}}},
        "required": True,
    },
    responses={
        200: "Successful response",
        400: "Bad request",
    },
    operation_id="User",
    tags=["User"],
    deprecated=False,
    summary="Get Sample",
    ),
    post=extend_schema(
        description="This is a custom view that does something awesome.",
    parameters=[
        {
            "name": "param1",
            "in": "query",
            "type": "integer",
            "description": "A query parameter",
            "required": False,
        },
    ],
    request={
        "content": {"application/json": {"schema": {"type": "object"}}},
        "required": True,
    },
    responses={
        200: "Successful response",
        400: "Bad request",
    },
    operation_id="User",
    tags=["User"],
    deprecated=False,
    summary="Post Sample",
    )
    )
class SampleTest(APIView):

    
    def get(self,request):
        error_log.error("wrongs")
        print(request.user)
        return Response({'test':'ok'})
    def post(self,request):
        return Response({'test':'ok'})
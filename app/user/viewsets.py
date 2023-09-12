from rest_framework.views import APIView
from rest_framework.response import Response
from core.logger import error_log
from drf_spectacular.utils import extend_schema,extend_schema_view,OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .serializers import SampleSerializer,ExcelSampleSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Demo,ExcelDemo
import pandas as pd
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated





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
class SampleTest(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = SampleSerializer
    queryset = Demo.objects.all()
    
    # def get(self,request):
    #     error_log.error("wrongs")
    #     print(request.user)
    #     return Response({'test':'ok'})
    # def post(self,request):
    #     return Response({'test':'ok'})

class ExcelSampleView(APIView):
    parser_classes=(MultiPartParser,FormParser,JSONParser)
    serializer_class = ExcelSampleSerializer
    
    def post(self,request):
        file = request.data.get('excel')
        if file:
            read_file = pd.read_excel(file)
            read_file.fillna('', inplace=True)
            print(read_file.iterrows(),"][]")
            for index,row in read_file.iterrows():
                data = {column_name.lower(): cell_value for column_name, cell_value in row[1:].items()}
                try:
                    ExcelDemo.objects.create(**data)
                except Exception as e:
                    print(str(e))
                print(data)
   
            return Response({'message': 'File uploaded and processed successfully'})
        else:
            return Response({'message': 'No file provided'}, status=400)
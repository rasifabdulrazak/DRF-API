"""
This file keeps the url routers of user app
"""

from django.urls import path,include
from .viewsets import SampleTest,ExcelSampleView

urlpatterns = [
    path('test/',SampleTest.as_view(),name='test'),
    path('file-upload/',ExcelSampleView.as_view(),name='file-upload')
]
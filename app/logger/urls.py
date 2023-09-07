"""
This file keeps the urls configuration of logger app
"""

from django.urls import path,include
from .views import DownloadErrorLog,DownloadCriticalLog

urlpatterns = [
    path('download/critical-log/',DownloadCriticalLog.as_view(),name='download-critical-log'),
    path('download/error-log/',DownloadErrorLog.as_view(),name='download-error-log')
]
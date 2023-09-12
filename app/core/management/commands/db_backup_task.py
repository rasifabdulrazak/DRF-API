"""
This keep the dbbackup function
"""
from django.core.management.base import BaseCommand
from ...tasks import db_backup_task
from datetime import datetime
import os
from django.core.management import call_command
from ...logger import critical_log
from ...tasks import db_backup_task
class Command(BaseCommand):
    help = 'Perform database backup'

    def handle(self, *args, **kwargs):
        try:
            db_backup_task()
            self.stdout.write(self.style.SUCCESS('Database backup completed successfully.'))
        except Exception as e:
            print(str(e))
            critical_log.error(f"Something went wrong: {str(e)}")
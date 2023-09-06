"""
This keep the dbbackup function
"""
from django.core.management.base import BaseCommand
from ...tasks import db_backup_task
from datetime import datetime
import os
from django.core.management import call_command
from ...logger import critical_log

class Command(BaseCommand):
    help = 'Perform database backup'

    def handle(self, *args, **kwargs):
        try:
            path = '/backups'
            # delete old files in server to reduce the memory space
            if os.path.exists(path):
                list_of_files = os.listdir(path)
                for name in list_of_files:
                    file_path = os.path.join(path,name)
                    if os.path.isfile(file_path):
                        print("deleting the old files")
                        os.remove(file_path)

            # Generate a filename without spaces or special characters
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            name = f"DRF-API-BACKUP-{timestamp}.dump"

            # Call the dbbackup command with the filename to create
            call_command("dbbackup", output_filename=name)

            self.stdout.write(self.style.SUCCESS('Database backup completed successfully.'))
        except Exception as e:
            print(str(e))
            critical_log.error(f"Something went wrong: {str(e)}")
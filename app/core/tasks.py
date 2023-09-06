"""
This file keep the tasks
"""
from datetime import datetime
from django.core.management import call_command
from .logger import error_log,critical_log
import os


def db_backup_task():
    """
    celery beat task for creating db backup
    """
    #! db backup through shell script disabled
    #! django db_backup using instead of script.
    # script = os.path.join("scripts", "db_backup.sh")
    # subprocess.call(["bash", script])
    try:
        path = '/backups/'
        if os.path.exists(path):
            print("Folder Found")
            list_of_files = os.listdir(path)
            for name in list_of_files:
                file_path = os.path.join(path,name)
                if os.path.isfile(file_path):
                    print("deleting the old files")
                    os.remove(file_path)
        # Generate a filename without spaces or special characters
        # timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name = f"DRF-API-BACKUP.dump"

        # Call the dbbackup command without the -o option
        call_command("dbbackup", output=name)

    except Exception as e:
        print(str(e))
        critical_log.error(f"Something went wrong : {str(e)}")

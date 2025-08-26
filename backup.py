import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_files_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_files_name, 'gztar', source)

# These lines should be outside the function
source = "/home/kashifali/Downloads/python-workshop-practice"
destination = "/home/kashifali/Downloads/python-workshop-practice/backups"

backup_files(source, destination)

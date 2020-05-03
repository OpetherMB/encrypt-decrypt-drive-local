from context import service
import os

drive_service = service.DriveService(os.path.join('credentials','credentials.json') )
drive_service.auth()

folder = drive_service.create_folder('Maro_test')
file = drive_service.upload_file('data_test', 'C:/Users/hp/Documents/Python-Scripts/Python-File-Encryptor/data_test.txt', folder)
link = drive_service.anyone_permission(file)

print(file)
print(link)
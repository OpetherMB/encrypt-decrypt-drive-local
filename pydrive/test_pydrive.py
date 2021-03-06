from context import service

drive_service = service.DriveService('./client_secret.json')
drive_service.auth()

folder = drive_service.create_folder('Xesque')
file = drive_service.upload_file('', './maro.txt', folder)
link = drive_service.anyone_permission(file)

print(file)
print(link)
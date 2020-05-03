  
from context import service
import requests
import  os


drive_service = service.DriveService(os.path.join('credentials','credentials.json') )
drive_service.auth()

name= 'marouane'
files = drive_service.list_files_by_name(name)

# folder_id =files[0]['id']
# drive_service.list_files_from_folder_id(folder_id=folder_id)
print('\n')
print(' ')

url = ''

for file in files:#
     f = drive_service.get_file_info(file['id'])
     print(f)

     url = f['webContentLink']

# download content

r = requests.get(url, stream=True)

with open(os.path.join('encrypt', name+'.encrypted' ), 'wb') as f:
     for chunk in r.iter_content():
           f.write(chunk)
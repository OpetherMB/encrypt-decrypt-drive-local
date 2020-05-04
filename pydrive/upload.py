from context import service
from enc2dec import Encryption_
import getpass
import os


File_to_encrypt = r'hichame.txt'
input_folder = r'C:\Users\hp\Documents\Python-Scripts\Python-File-Encryptor\local_files_to_encrypt'

destination_file = r'C:\Users\hp\Documents\Python-Scripts\Python-File-Encryptor\encrypted' 



# with open(path_encrypt, 'rb') as f:
#      print(f.read() )

# print(path_encrypt)
###


try: 
        print("enter the key for encryption")
        key = getpass.getpass()

        key = bytes(key, encoding='utf-8')
        print(key)

except Exception as error:
        print('ERROR', error)

Encryption_(destination_file, input_folder , True , File_to_encrypt  , key)

# # think about deleting it 

drive_service = service.DriveService(r"C:\Users\hp\Documents\Python-Scripts\Python-File-Encryptor\credentials\credentials.json" )
# print(os.path.join(r"C:\Users\hp\Documents\Python-Scripts\Python-File-Encryptor\credentials",'credentials.json'))

drive_service.auth()

folder = drive_service.create_folder('hichame_test')
file = drive_service.upload_file( File_to_encrypt.split('.')[0] , os.path.join(destination_file,File_to_encrypt.split('.txt')[0]+'.encrypted' ),  folder)
link = drive_service.anyone_permission(file)

print(file)
print(link)


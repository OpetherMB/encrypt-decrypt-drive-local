# -*- coding: utf-8 -*-
"""
wrote by marouane benmoussa

this code ...

"""

# C:/Users/hp/Anaconda3/envs/Datascience/python.exe  c:/Users/hp/Documents/Python-Scripts/Python-File-Encryptor/enc2dec.py  
# --input_file  c:\Users\hp\Documents\Python-Scripts\Python-File-Encryptor\decrypt  --dst_file  c:\Users\hp\Documents\Python-Scripts\Python-File-Encryptor\encrypt  --encrypt False --decrypt True --filewanted 
# caf.encrypted

import sys
import os
import getpass
import docx
from cryptography.fernet import Fernet
import argparse

# required arg




    


import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# # change type from docx to txt
# input_file = '/content/drive/My Drive/temp'

# for File in os.listdir(input_file): 
#   if File.endswith('.docx'):
#       doc = docx.Document(os.path.join(input_file,File) )
#       result = [p.text for p in doc.paragraphs]

#       with open(os.path.join(input_file , File.split('.docx')[0]+".txt") , 'w') as f:
#             f.writelines("%s\n" % line for line in result)
#             f.close()

# add gdoc reader

def send_mail(sender_email, receiver_email, subject, password , output_file ):

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = output_file  

    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def encrypt_file(input_folder , destination_file, File, key):

          input_file = os.path.join(input_folder, File )
          output_file = os.path.join(destination_file, File.split('.txt')[0]+'.encrypted')

          with open(input_file, 'rb') as f:
              data = f.read()

          fernet = Fernet(key)
          encrypted = fernet.encrypt(data)

          with open(output_file, 'wb') as f:
              f.write(encrypted)

          return output_file      



def Encryption_(destination_file, input_folder , flag , FileWanted , key):

    if flag :
        output_file = encrypt_file(input_folder , destination_file, FileWanted, key)
        return output_file


    else :
        for File in os.listdir(input_folder):
            encrypt_file(input_folder , destination_file, File, key)
        
        return destination_file



# You can delete input_file if you want
# And then to decrypt a file:

def decryption_file(destination_file, File, input_folder, key):
    
         input_file =  os.path.join(destination_file, File )
         outp_ext = File.split('.encrypted')[0]+'.txt'
         output_file =  os.path.join(input_folder, outp_ext )

         with open(input_file, 'rb') as f:
                  data = f.read()

         fernet = Fernet(key)
         encrypted = fernet.decrypt(data)

         with open(output_file, 'wb') as f:
                  f.write(encrypted)

         return output_file                  


def Decryption_(destination_file, input_folder, FileWanted, password ,key , flag ,send_mail ):
      
      if flag : 
              
              output_file = decryption_file(destination_file, FileWanted, input_folder, key)
              send_mail(sender_email, receiver_email, subject, password , output_file)
              print("mail was sent...")

      else :

          for File in os.listdir(destination_file):
              output_file = decryption_file(destination_file, File, input_folder, key)
              send_mail(sender_email, receiver_email, subject, password , output_file)
              print("mail was sent...")




if __name__ == "__main__":


    parser = argparse.ArgumentParser()

    parser.add_argument('--input_file', required=True)
    parser.add_argument('--dst_file', required=True)
    parser.add_argument('--encrypt', required=True)
    parser.add_argument('--decrypt', required=True)
    parser.add_argument('--filewanted', required=True)

    
    args = parser.parse_args()

    ########
    
    input_folder = args.input_file
    destination_file = args.dst_file
    ###email data 

    subject = "crypted data from drive to you"
    body = "This is an email with attachment sent from Python"
    sender_email = "******@gmail.com"
    receiver_email = "*******@outlook.com"
    ### args

    send_email = True
    encrypt = args.encrypt
    decrypt = args.decrypt
    FileWanted = args.filewanted
    
    flag = True
    delete_local = True
    ###

    if send_email:
        try: 
            print("enter email app code ! ")
            password  = getpass.getpass() 
        except Exception as error: 
            print('ERROR', error) 


    try: 
        print("enter the key for encryption")
        key = getpass.getpass()

        key = bytes(key, encoding='utf-8')
        print(key)

    except Exception as error:
        print('ERROR', error)


    if encrypt : 
        Encryption_(destination_file, input_folder , flag , FileWanted , key)

    if decrypt : 
        Decryption_(destination_file, input_folder,FileWanted , password, key, True ,send_mail) 


    key = " "
    password = " "

    if delete_local : 
    # delete all data 
         [ os.remove(os.path.join(input_folder , File) ) for File in os.listdir(input_folder) ]


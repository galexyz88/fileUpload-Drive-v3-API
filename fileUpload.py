from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import Error, HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
    
    
    #Removing the old folder if it exists
    try:
        page_token = None
        while True:
            #Change the folder name
            response = service.files().list(q="name='New Folder' and mimeType = 'application/vnd.google-apps.folder'",
                                                spaces='drive').execute()
            for file in response.get('files', []):
                # Process change
                print('Found folder: %s (%s) to be deleted' % (file.get('name'), file.get('id')))
                service.files().delete(fileId=file.get('id')).execute()
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
    except HttpError as e:
        print(e)
    except Error as e:
        print(e)
        
           
     #Creating a new/updated folder in drive for the files to live in (rename as required.)
    file_metadata_folder = {
    'name': 'New Folder',
    'mimeType': 'application/vnd.google-apps.folder'
}
    fileFolder = service.files().create(body=file_metadata_folder,
                                    fields='id').execute()
    folder_id = fileFolder.get('id')
    folder_name = file_metadata_folder.get('name')

    #Uploads list of files to be stored within a folder in Drive. The following will be an example list          
    file_names = ["text1.txt", "text2.txt", "photo.jpg"]
    print("New Folder: %s (%s) created within Drive." % (folder_name, folder_id))
    for name in file_names:
        file_metadata = {'name': name,
                         'parents': [folder_id]
        }
        media = MediaFileUpload(name, mimetype='text/plain')
        file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
        print('Updated File: %s stored in Folder: New Folder (%s)' % (name, folder_id))

if __name__ == '__main__':
    main()
    

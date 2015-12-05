from __future__ import print_function
import httplib2
import os
import apiclient
import encrypt_module

from apiclient import discovery
from apiclient import errors
from apiclient import http
from apiclient.http import MediaFileUpload
from apiclient.http import MediaIoBaseDownload

import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

import sys
from PyQt4 import QtCore, QtGui

from encryptor_ui import Ui_LoadPage
from upload_ui import Ui_UploadDialog
from download_ui import Ui_DownloadDialog


SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Encryptor'

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'drive-python-encryptor.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def upload_file(service, title, mime_type, parent_id, filename):
    if filename:
        media_body = MediaFileUpload(filename, mimetype=mime_type, resumable=True)
    else:
        media_body=None
        
    body = {
        'title': title,
          }
    # Set the parent folder.
    if parent_id:
        body['parents'] = [{'id': parent_id}]
    # Set the MIME type.
    if mime_type:
        body['mimeType']= mime_type

    try:
        file = service.files().insert(body=body,media_body=media_body).execute()
        return file
    except errors.HttpError, error:
        print ('An error occured: %s' % error)
        return None

def download_file(service, file_id, local_fd):
    request = service.files().get_media(fileId=file_id)
    media_request = MediaIoBaseDownload(local_fd, request)

    while True:
        try:
            download_progress, done = media_request.next_chunk()
        except errors.HttpError, error:
            print ('An error occurred: %s' % error)
            return
        if download_progress:
            print ('Download Progress: %d%%' % int(download_progress.progress() * 100))
        if done:
            print ('Download Complete')
            return

def get_files_in_folder(service, folder_id):
    page_token = None
    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token
            children = service.children().list(folderId=folder_id, **param).execute()
            files=[]
            for child in children.get('items', []):
                file = service.files().get(fileId=child['id']).execute()
                file['id']=child['id']
                files.append(file)
            page_token = children.get('nextPageToken')
            if not page_token:
                break
        except errors.HttpError, error:
            print ('An error occurred: %s' % error)
            break
    return files     

credentials = get_credentials()
http = credentials.authorize(httplib2.Http())      
service = discovery.build('drive', 'v2',http=http)

about = service.about().get().execute()
root=about['rootFolderId']

results = service.files().list().execute()
items = results.get('items', [])

for item in items:
    if item['title']=='Encrypted' and item['mimeType']=='application/vnd.google-apps.folder':
        folderID=item['id']
        break
    else:
        folderID=None

if folderID==None:
    try:
        createdFolder=upload_file(service,'Encrypted','application/vnd.google-apps.folder',root,None)
        folderID=createdFolder['id']
    except errors.HttpError, error:
        print ('An error occured: %s' % error)        

class LoadPage(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_LoadPage()
        self.ui.setupUi(self)
        self.ui.uploadButton.clicked.connect(self.handleUpload)
        self.ui.downloadButton.clicked.connect(self.handleDownload)
        self.nextPageU=None
        self.nextPageD=None

    def handleUpload(self):
        if self.nextPageU is None:
            self.nextPageU = UploadDialog(self)
        self.nextPageU.show()

    def handleDownload(self):
        if self.nextPageD is None:
            self.nextPageD = DownloadDialog(self)
        self.nextPageD.show()
        
class UploadDialog(QtGui.QMainWindow):
    def __init__(self,parent=LoadPage):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_UploadDialog()
        self.ui.setupUi(self)
        self.ui.browseButton.clicked.connect(self.handleBrowse)
        self.ui.uploadButton.clicked.connect(self.handleUpload)

    def handleBrowse(self):
        fileaddress = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.ui.address.setText(fileaddress)

    def handleUpload(self):
        filepath=str(self.ui.address.displayText())
        key= encrypt_module.readfile('key.inc', 'rb')
        plaintext = encrypt_module.readfile(filepath, 'rb')
        e_filepath=encrypt_module.encrypt(plaintext,filepath,key)
        e_filename=e_filepath.split('/')[-1]
        fileid=upload_file(service,e_filename,'application/octet-stream',folderID,e_filepath)
        os.remove(e_filepath)
        #QtCore.QCoreApplication.instance().quit()

class DownloadDialog(QtGui.QMainWindow):
    def __init__(self,parent=LoadPage):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_DownloadDialog()
        self.ui.setupUi(self)
        self.ui.downloadButton.clicked.connect(self.handleDownload)
        files=get_files_in_folder(service,folderID)
        filenameList=[file['title'] for file in files]
        self.ui.fileList.clear()
        self.ui.fileList.addItems(filenameList)

    def handleDownload(self):
        filename=str(self.ui.fileList.currentItem().text())
        files=get_files_in_folder(service,folderID)
        for file in files:
            if file['title']==filename:
                fileID=file['id']
                break
            else:
                fileID=None
        if fileID:
            fw=open('EncryptedDownloads/'+filename ,'wb')
            download_file(service,fileID,fw)
            fw.close()
            key= encrypt_module.readfile('key.inc', 'rb')
            encrypt_module.decrypt(key,'EncryptedDownloads/'+filename)
            os.remove('EncryptedDownloads/'+filename)
def main():
    app = QtGui.QApplication(sys.argv)
    myapp = LoadPage()
    myapp.show()
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()     
        

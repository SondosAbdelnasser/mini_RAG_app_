from fastapi import UploadFile
from.BaseController import BaseController 
class DataController:
    def __init__(self):
        super().__init__()
    def validate_uploaded_file(self,file:UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False  
        if file.size >self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False
        return True
 
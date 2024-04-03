from Camera import Camera
from ICamera import ICamera
from settings.SettingsHandler import SettingsHandlerSingleton as SettingsHandler

class DetectorApp:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DetectorApp, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.cam_details = []
        self.init_cameras()
        self.settings_handler = SettingsHandler()
        self.camera_objects = {}
    
    def init_cameras(self):
        
        self.cam_details = self.settings_handler.get_camera_info()
        
        for cam in self.cam_details:
            cam_obj = Camera(cam['id'], cam['name'], None)
            
            self.camera_objects[cam['id']] = cam_obj
            cam_obj.arm()
            cam_obj.start_streaming()
    
    def get_cameras(self):
        return self.camera_objects

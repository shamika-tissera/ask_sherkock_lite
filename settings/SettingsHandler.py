import yaml

class SettingsHandlerSingleton:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SettingsHandlerSingleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.settings = None
        self.load_settings()
        
    def load_settings(self):
        try:
            with open('config.yaml', 'r') as file:
                self.settings = yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Config file not found")
            
    def get_settings(self):
        return self.settings
    
    def get_dvr_info(self):
        ip = self.settings['dvr']['ip']
        port = self.settings['dvr']['port']
        user = self.settings['dvr']['user']
        password = self.settings['dvr']['password']
        make = self.settings['dvr']['make']
        return ip, port, user, password, make
    
    def get_camera_info(self):
        return self.settings['cameras']
    
    def get_camera_ids(self):
        return [camera['id'] for camera in self.get_camera_info()]
    

# obj = SettingsHandlerSingleton()

# cam_details = obj.get_camera_info()


# print(obj.get_camera_info())

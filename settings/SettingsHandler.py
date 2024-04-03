import yaml
import os

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
            # Get the directory of this script
            script_dir = os.path.dirname(os.path.realpath(__file__))
            # Construct the full path to the config file
            config_path = os.path.join(script_dir, './config/config.yaml')
            with open(config_path, 'r') as file:
                self.settings = yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Config file not found")
            
    def get_settings(self):
        return self.settings
    
    def get_dvr_info(self):
        ip = self.settings['network']['dvr']['ip']
        port = self.settings['network']['dvr']['port']
        user = self.settings['network']['dvr']['username']
        password = self.settings['network']['dvr']['password']
        make = self.settings['network']['dvr']['make']
        return ip, port, user, password, make
    
    def get_camera_info(self):
        return self.settings['cameras']
    
    def get_camera_ids(self):
        return [camera['id'] for camera in self.get_camera_info()]

import cv2
import threading
import queue

from detections.ObjectDetector import ObjectDetector
from detections import person
from ICamera import ICamera
from settings.SettingsHandler import SettingsHandlerSingleton
import constants


class Camera(ICamera):
    # cap = cv2.VideoCapture('./videos/street.mp4')
    
    def __init__(self, camera_id, name):
        self.check_dvr_compatibility()
        self.armed = False
        self.camera_thread = None
        self.camera_id = camera_id
        self.current_frame = None  # attribute to store the current frame
        self.frame_queue = queue.Queue()
        self.name = name
        self.cap = cv2.VideoCapture('./videos/street.mp4')
        self.self_settings_handler_singleton = SettingsHandlerSingleton()
        
    def check_dvr_compatibility(self):
        self.settings_handler_singleton = SettingsHandlerSingleton()
        dvr_info = self.settings_handler_singleton.get_dvr_info()
        _, _, _, _, make = dvr_info
        if (make not in constants.SUPPORTED_DVRS):
            raise Exception(f"{make} is not a supported DVR make")
        
    def arm(self):
        self.camera_thread = threading.Thread(target=self.run)
        self.camera_thread.start()
        self.armed = True
        print("Camera armed")
    
    def start_streaming(self):
        print(f"Streaming from {self.camera_id}")
        def stream():
            while True:
                ret, frame = self.cap.read()
                if ret:
                    # self.frame_queue.put(frame)  # Add the new frame to the queue
                    self.current_frame = frame  # Update the current frame

        streaming_thread = threading.Thread(target=stream)
        streaming_thread.start()
        
    def get_rtsp_base_url(self):
        # e.g.: rtsp://admin:admin123@192.168.1.102:554/Streaming/channels/101
        ip, port, user, password, _ = self.self_settings_handler_singleton.get_dvr_info()
        return f"rtsp://{user}:{password}@{ip}:{port}/Streaming/channels/"
    
    def get_raw_frame_copy(self):
        if self.current_frame is not None:
            return self.current_frame.copy()  # Return a copy of the current frame
        return None
        
    def run(self):
        i = 0
        obj_detector = ObjectDetector('person')
        while True:
            i += 1
            if self.armed:
                frame = self.frame_queue.get()
                count = obj_detector.count(frame)

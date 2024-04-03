from ultralytics import YOLO
import cv2

class ObjectDetector:
    def __init__(self, detection_object):
        self.detection_object = detection_object
        self.model = YOLO('yolov8m.pt')
        
    def count(self, frame):
        results = self.model(frame)
        names = self.model.names
        detection_object_id = list(names)[list(names.values()).index(self.detection_object)]
        return results[0].boxes.cls.tolist().count(detection_object_id)

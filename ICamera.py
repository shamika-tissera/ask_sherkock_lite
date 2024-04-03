from abc import ABC, abstractmethod


class ICamera(ABC):
    
    @abstractmethod
    def arm(self):
        pass
    
    @abstractmethod
    def start_streaming(self):
        pass
        
    @abstractmethod
    def get_raw_frame_copy(self):
        pass
        
    @abstractmethod
    def run(self):
        pass        

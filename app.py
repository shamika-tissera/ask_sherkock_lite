from DetectorApp import DetectorApp
from flask import Flask

app = Flask(__name__)

detector_app = DetectorApp()
detector_app.init_cameras()

@app.route('/')
def camera_stream(camera_id):
    camera = detector_app.get_camera(1)
    
    while True:
        frame = camera.get_raw_frame_copy()
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + b'\r\n\r\n')
            

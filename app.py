from DetectorApp import DetectorApp
from flask import Flask

app = Flask(__name__)

detector_app = DetectorApp()
detector_app.init_cameras()

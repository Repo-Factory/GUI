from PyQt5 import QtWidgets, uic
from resources import CONTROL_UI

class PIDController(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(CONTROL_UI, self)  # Load the .ui file for the new window

from PyQt5 import QtWidgets, uic
from path_concat import ui_path

CONTROL_UI = ui_path('pid_control.ui')
class PIDController(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(CONTROL_UI, self)  # Load the .ui file for the new window

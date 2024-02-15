from PyQt5.QtCore import QObject
from controller.pid_control import PIDController

class AddPage(QObject):
    def __init__(self, main):
        super().__init__()
        self.main = main
    
    def add_widgets(self):
        self.main.pid_page = PIDController()
        self.main.stacked_widget.addWidget(self.main.pid_page)

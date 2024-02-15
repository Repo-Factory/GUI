from PyQt5 import QtWidgets, uic
from navigate_pages import ButtonActions
from add_pages import AddPage
from icons import Icons
from resources import MAINWINDOW_UI_FILE

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(MAINWINDOW_UI_FILE, self)

        add_page = AddPage(self)
        add_page.add_widgets()

        button_handler = ButtonActions(self)
        button_handler.connect_buttons()
        
        icons = Icons(self)
        icons.setIcons()
        
        self.stacked_widget.setCurrentIndex(0)  # Set the initial page to index 0
        
        
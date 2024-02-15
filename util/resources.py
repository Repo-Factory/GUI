import os

def ui_path(filename):
    UI_DIRECTORY = 'ui'
    return os.path.join(UI_DIRECTORY, filename)

def styles_path(filename):
    STYLES_DIRECTORY = 'styles'
    return os.path.join(STYLES_DIRECTORY, filename)

CONTROL_UI = ui_path('pid_control.ui')
MAINWINDOW_UI_FILE = ui_path('mainwindow.ui')
STYLESHEET = styles_path("indigo.qss")
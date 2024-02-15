from PyQt5.QtWidgets import QCheckBox, QTextEdit
from PyQt5.QtCore import QObject
import re
import subprocess

class Launch(QObject):
    def __init__(self, main):
        self.main = main


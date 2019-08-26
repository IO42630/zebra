

import sys
from PyQt5.QtWidgets import QFileDialog




class Tools():


    def __init__(self):
        pass


    def open_file(self, container):
        ''' Corresponds to 1.2
        TODO Right now this is just copy&pasted. Clean this up.'''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(container,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName
        pass

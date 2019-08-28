

import sys
from PyQt5.QtWidgets import QFileDialog, QTableWidget, QPlainTextEdit,QWidget




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



class Table(QTableWidget):
    def __init__(self):
        super().__init__()

        self.setSortingEnabled(True)

        self.setRowCount(4)
        self.setColumnCount(4)

        self.setMinimumSize(300,200)

        self.setHorizontalHeaderLabels({'h', 'k', 'l'})








class Text(QPlainTextEdit):
    def __init__(self, text):
        super().__init__()
        self.setMinimumSize(200,200)
        self.setPlainText(text)


class View():
    def __init__(self):
        pass


    def show(self):
        ''' Show widgets. '''
        #TODO filter this, so that it applies to QWidgets only.
        for widget in vars(self):
            vars(self)[widget].setHidden(False)

    def hide(self):
        ''' Hide widgets. '''
        for widget in vars(self):
            vars(self)[widget].setHidden(True)







from PyQt5.QtWidgets import QPlainTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem

from PyQt5.QtGui import QPixmap


class WelcomeView(QWidget):

    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.zebraLabel = QLabel()
        zebraImage = QPixmap('zebra.png')
        self.zebraLabel.setPixmap(zebraImage)
        self.vbox.addWidget(self.zebraLabel)

        self.note = QLabel('Please select a Mode.')
        self.vbox.addWidget(self.note)
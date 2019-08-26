import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QLabel, QVBoxLayout, QWidget

from two_d_mode import TwoDMode
from one_d_mode import OneDMode, OneDTable



class TestAWidget(QMainWindow):



    def __init__(self):
        ''' Replace `QPushButton` with any widget you intend to test.
        This is meant to be used for quick and easy testing.'''
        super().__init__()


        self.testWidget = OneDMode()




        self.setCentralWidget(self.testWidget)
        self.setGeometry(0,0,400,400)
        self.setWindowTitle('Test')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = TestAWidget()
    sys.exit(app.exec())
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGraphicsPixmapItem, QLabel,QWidget, QVBoxLayout, QAction
from twoDimView import TwoDimView
from oneDimView import OneDimView
from welcomeView import WelcomeView
from zebraView import ZebraView




class Zebra(QMainWindow):


    def __init__(self):
        ''' The main window of the Zebra application.'''
        super().__init__()

        # Set the main container.
        self.container = QWidget(self)
        self.setCentralWidget(self.container)

        # Set the main layout.
        self.vbox = QVBoxLayout()
        self.container.setLayout(self.vbox)

        # Add things.
        self.addViews()
        self.mainMenu()

        # Finalize settings and show.
        self.setGeometry(0,0,0,0)
        self.setWindowTitle('Zebra')
        self.show()


    def addViews(self):
        ''' Add the three views.'''
        self.welcomeView = WelcomeView()
        self.vbox.addWidget(self.welcomeView)
        self.welcomeView.setHidden(False)

        self.zebraView = ZebraView()
        self.vbox.addWidget(self.zebraView)
        self.zebraView.setHidden(True)

        self.oneDimView = OneDimView()
        self.vbox.addWidget(self.oneDimView)
        self.oneDimView.setHidden(True)

        self.twoDimView = TwoDimView()
        self.vbox.addWidget(self.twoDimView)
        self.twoDimView.setHidden(True)


    def mainMenu(self):
        ''' Set up the main menu.'''
        self.modeMenu = self.menuBar().addMenu('Mode')

        self.zebraMenuEntry = QAction('Zebra')
        self.zebraMenuEntry.triggered.connect(lambda: self.showView('zebra'))
        self.modeMenu.addAction(self.zebraMenuEntry)

        self.oneDMenuEntry = QAction('1D Mode')
        self.oneDMenuEntry.triggered.connect(lambda: self.showView('1D'))
        self.modeMenu.addAction(self.oneDMenuEntry)

        self.twoDMenuEntry = QAction('2D Mode')
        self.twoDMenuEntry.triggered.connect(lambda: self.showView('2D'))
        self.modeMenu.addAction(self.twoDMenuEntry)



    def showView(self, view):
        self.welcomeView.setHidden(True)
        self.zebraView.setHidden(True)
        self.oneDimView.setHidden(True)
        self.twoDimView.setHidden(True)

        if view == 'zebra':
            self.zebraView.setHidden(False)
        elif view == '1D':
            self.oneDimView.setHidden(False)
        elif view =='2D':
            self.twoDimView.setHidden(False)
        else:
            pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Zebra()
    sys.exit(app.exec())
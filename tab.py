
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget ,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        ''' Everything is used with `self.` so it can be easily accessed in any function.
        '''
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 0
        self.top = 0
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, 400, 400)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.modeMenu = self.menuBar().addMenu('Mode')

        self.zebraMenuEntry = QAction('Zebra')
        self.zebraMenuEntry.triggered.connect(self.close)
        self.modeMenu.addAction(self.zebraMenuEntry)

        self.oneDMenuEntry = QAction('1D Mode')
        self.oneDMenuEntry.triggered.connect(self.close)
        self.modeMenu.addAction(self.oneDMenuEntry)

        self.twoDMenuEntry = QAction('2D Mode')
        self.twoDMenuEntry.triggered.connect(self.close)
        self.modeMenu.addAction(self.twoDMenuEntry)



        self.show() # once everything is set up, show the window.





class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)





        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300 ,200)

        # Add tabs
        self.tabs.addTab(self.tab1 ,"Prep Experiment Zebra")
        self.tabs.addTab(self.tab2 ,"1D Mode")
        self.tabs.addTab(self.tab3, "2D Mode")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)


        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.tabs2 = QTabWidget()
        self.tab21 = QWidget()
        self.tabs2.addTab(self.tab21, "hello")
        self.tab2.layout.addWidget(self.tabs2)


        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
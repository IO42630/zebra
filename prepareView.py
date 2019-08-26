


from PyQt5.QtWidgets import QPlainTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem

from PyQt5.QtGui import QPixmap
from tools import Tools

class PrepareView(QWidget):

    def __init__(self):
        ''' Widget containing the entire Zebra Mode view. '''
        super().__init__()

        self.grid = QGridLayout()

        self.setLayout(self.grid)

        self.define_widgets()
        self.showView('none')
        self.set_widget_actions()




    def define_widgets(self):
        ''' Define widgets such as buttons. This must be done before setting widget actions.
        Otherwise a widget action might try to modify a widget that is not defined yet.'''

        # add empty label as spacer after buttons
        # this has some side effects (i suspect) :
        # + when adding the Buttons20, we really mean for it to span from grid position (3,1) to (3,2)
        # but to create the correct visual effect it must span also over the invisible spacder column,
        # Thus from (3,1) to (3,3).
        self.grid.addWidget(QLabel(), 10,10)


        # Common items


        self.buttons00 = Buttons00(self)
        self.grid.addWidget(self.buttons00,0,0)



        # Zebra Nuc View

        self.nucTable = OneDTable()
        self.grid.addWidget(self.nucTable,0,1)


        self.nucButtons11 = NucButtons11(self)
        self.grid.addWidget(self.nucButtons11, 1,1)




        #self.buttons20 = Buttons20()
        #self.grid.addWidget(self.buttons20, 2,0)

        #self.buttons30 = Buttons30()
        #self.grid.addWidget(self.buttons30, 3,0)




        # Zebra Mag View

        self.magTable = OneDTable()
        self.grid.addWidget(self.magTable,0,1)

        self.magButtons11 = MagButtons11(self)
        self.grid.addWidget(self.magButtons11,1,1)

        self.magVisual = OneDText()
        self.grid.addWidget(self.magVisual, 0,2)

        self.magButtons12 = MagButtons12(self)
        self.grid.addWidget(self.magButtons12,1,2)





    def set_widget_actions(self):
        self.crystalFile = self.loadCrystalFileButton.clicked.connect(lambda: Tools().open_file(self))
        self.instrumentFile = self.loadInstrumentFileButton.clicked.connect(lambda: Tools().open_file(self))

        self.sectorNucButton.clicked.connect(lambda: self.showView('nuc'))
        self.sectorMagButton.clicked.connect(lambda: self.showView('mag'))
        pass



    def showView(self,view):
        ''' Will hide everything if called with anything besides nuc or mag.'''
        self.nucTable.setHidden(True)
        self.nucButtons11.setHidden(True)
        self.magTable.setHidden(True)
        self.magButtons11.setHidden(True)
        self.magVisual.setHidden(True)
        self.magButtons12.setHidden(True)

        if view == 'nuc':
            self.nucTable.setHidden(False)
            self.nucButtons11.setHidden(False)
        elif view == 'mag':
            self.magTable.setHidden(False)
            self.magButtons11.setHidden(False)
            self.magVisual.setHidden(False)
            self.magButtons12.setHidden(False)
        else:
            pass




class OneDText(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200,200)
        self.setPlainText("List of Files:\n+ File 1\n+ File 2")



class OneDTable(QTableWidget):
    def __init__(self):
        super().__init__()

        self.setSortingEnabled(True)

        self.setRowCount(4)
        self.setColumnCount(4)

        self.setMinimumSize(300,200)

        self.setHorizontalHeaderLabels({'h', 'k', 'l'})



class Buttons00(QWidget):

    def __init__(self, c):
        ''' Here c stands for container, thus the main window.'''
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)
        self.set
        self.setFixedWidth(240)
        self.setFixedHeight(200)

        c.loadCrystalFileButton = QPushButton()
        c.loadCrystalFileButton.setText("Load Crystal File")
        grid.addWidget(c.loadCrystalFileButton, 0, 0)

        c.loadInstrumentFileButton = QPushButton()
        c.loadInstrumentFileButton.setText('Load Instrument File')
        grid.addWidget(c.loadInstrumentFileButton,1,0)

        c.sectorNucButton = QPushButton()
        c.sectorNucButton.setText('Sector Nuc')
        grid.addWidget(c.sectorNucButton,2,0)

        c.sectorMagButton = QPushButton()
        c.sectorMagButton.setText('Sector Mag')
        grid.addWidget(c.sectorMagButton,3,0)



class NucButtons11(QWidget):

    def __init__(self,c):
        ''' Here c stands for container, thus the main window.\n
        The purpose of this notation is to enable access to each button via self in the main window.'''
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        c.sortNucButton = QPushButton()
        c.sortNucButton.setText("Sort")
        grid.addWidget(c.sortNucButton,0,0)

        c.optimizeNucButton = QPushButton()
        c.optimizeNucButton.setText("Optimize")
        grid.addWidget(c.optimizeNucButton,0,1)

        c.saveNucButton = QPushButton()
        c.saveNucButton.setText("Save")
        grid.addWidget(c.saveNucButton,0,2)

class MagButtons11(QWidget):

    def __init__(self,c):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        c.runMagButton = QPushButton()
        c.runMagButton.setText("Run")
        grid.addWidget(c.runMagButton,0,0)

class MagButtons12(QWidget):

    def __init__(self,c):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        c.sortMagButton = QPushButton()
        c.sortMagButton.setText("Sort")
        grid.addWidget(c.sortMagButton,0,0)

        c.optimizeMagButton = QPushButton()
        c.optimizeMagButton.setText("Optimize")
        grid.addWidget(c.optimizeMagButton,0,1)

        c.saveMagButton = QPushButton()
        c.saveMagButton.setText("Save")
        grid.addWidget(c.saveMagButton,0,2)













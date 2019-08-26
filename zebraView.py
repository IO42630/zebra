


from PyQt5.QtWidgets import QPlainTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem

from PyQt5.QtGui import QPixmap


class ZebraView(QWidget):

    def __init__(self):
        ''' Widget containing the entire Zebra Mode view. '''
        super().__init__()

        self.grid = QGridLayout()

        self.setLayout(self.grid)


        self.define_widgets()
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


        self.buttons00 = Buttons00()
        self.grid.addWidget(self.buttons00,0,0)



        # Zebra Nuc View

        self.nucTable = OneDTable()
        self.grid.addWidget(self.nucTable,0,1)


        self.nucButtons11 = NucButtons11()
        self.grid.addWidget(self.nucButtons11, 1,1)




        #self.buttons20 = Buttons20()
        #self.grid.addWidget(self.buttons20, 2,0)

        #self.buttons30 = Buttons30()
        #self.grid.addWidget(self.buttons30, 3,0)




        # Zebra Mag View

        self.magTable = OneDTable()
        self.magVisual = OneDText()




    def set_widget_actions(self):
        pass


    def showView(self,view):
        self.nucTable.setHidden(True)
        self.nucButtons11.setHidden(True)



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

    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        self.loadcrystalButton = QPushButton()
        self.loadcrystalButton.setText("Load Crystal File")
        grid.addWidget(self.loadcrystalButton, 0, 0)

        self.loadInstrumentFileButton = QPushButton()
        self.loadInstrumentFileButton.setText('Load Instrument File')
        grid.addWidget(self.loadInstrumentFileButton,1,0)

        self.sectorNucButton = QPushButton()
        self.sectorNucButton.setText('Sector Nuc')
        grid.addWidget(self.sectorNucButton,2,0)

        self.sectorMagButton = QPushButton()
        self.sectorMagButton.setText('Sector Mag')
        grid.addWidget(self.sectorMagButton,3,0)



class NucButtons11(QWidget):

    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        self.prepareNucButton = QPushButton()
        self.prepareNucButton.setText("Prepare")
        grid.addWidget(self.prepareNucButton,0,0)

        self.sortNucButton = QPushButton()
        self.sortNucButton.setText("Sort")
        grid.addWidget(self.sortNucButton,0,1)

        self.optimizeNucButton = QPushButton()
        self.optimizeNucButton.setText("Optimize")
        grid.addWidget(self.optimizeNucButton,0,2)

        self.saveNucButton = QPushButton()
        self.saveNucButton.setText("Save")
        grid.addWidget(self.saveNucButton,0,3)













from PyQt5.QtWidgets import QPlainTextEdit, QHBoxLayout, QWidget, QGridLayout, QLabel, QPushButton

from tools import Tools, View, Text, Table


class OneDimView(QWidget):


    def __init__(self):
        """ Widget containing the entire 2D Mode view. """
        super().__init__()

        # ----------------------------------------------------------------------
        # PREPARE
        # ----------------------------------------------------------------------

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Tools.View() groups Widgets for ease of use.
        self.one = View()

        # Define Files so IDE does not issue warnings (self. variables should be defined in __init__).
        self.dataFile = None

        # ----------------------------------------------------------------------
        # DEFINE WIDGETS
        # ----------------------------------------------------------------------

        # Add empty label as spacer after buttons.I suspect this has a side effect.
        # When adding Buttons20, we mean for them to span from grid position (3,1) to (3,2).
        # However to mainreate the mainorrect visual effect they must also mainover the invisible spacer mainolumn.
        # Thus we set them to span from grid position (3,1) to (3,3).
        self.grid.addWidget(QLabel(), 10, 10)

        #
        self.one.loadDataButton = QPushButton("Load Data File")
        self.one.loadDataButton.setMaximumWidth(200)
        self.grid.addWidget(self.one.loadDataButton, 0, 0)

        self.one.text = Text("List of Files:\n+ File 1\n+ File 2")
        self.grid.addWidget(self.one.text, 1, 0)

        self.one.table = Table()
        self.grid.addWidget(self.one.table, 0, 1, 4, 1)

        self.one.visualize = OneVisualize()
        self.grid.addWidget(self.one.visualize, 0, 2, 2, 2)

        self.one.buttons20 = Buttons20(self)
        self.grid.addWidget(self.one.buttons20, 2, 0)

        self.one.buttons30 = Buttons30(self)
        self.grid.addWidget(self.one.buttons30, 3, 0)

        self.one.buttons32 = Buttons32(self)
        self.grid.addWidget(self.one.buttons32, 3, 2)

        # ----------------------------------------------------------------------
        # SET WIDGET ACTIONS
        # ----------------------------------------------------------------------

        self.dataFile = self.one.loadDataButton.clicked.connect(lambda: Tools().open_file(self))

        # ----------------------------------------------------------------------
        # FINISH
        # ----------------------------------------------------------------------

        pass


class Buttons20(QWidget):

    def __init__(self, main):
        super().__init__()
        hbox = QHBoxLayout()
        self.setLayout(hbox)

        main.one.searchButton = QPushButton('Search')
        hbox.addWidget(main.one.searchButton)

        main.one.addButton = QPushButton('Add')
        hbox.addWidget(main.one.addButton)

        main.one.substractButton = QPushButton('Substract')
        hbox.addWidget(main.one.substractButton)


class Buttons30(QWidget):

    def __init__(self, main):
        super().__init__()
        hbox = QHBoxLayout()
        self.setLayout(hbox)

        main.one.integrateButton = QPushButton('Integrate')
        hbox.addWidget(main.one.integrateButton)

        main.one.lorentzButton = QPushButton('Lorentz')
        hbox.addWidget(main.one.lorentzButton)

        main.one.absorptionButton = QPushButton('Absorption')
        hbox.addWidget(main.one.absorptionButton)


class Buttons32(QWidget):
    """ Named after its position in the containing grid: row 3, column 2."""

    def __init__(self, main):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        main.one.saveButton = QPushButton('Save')
        grid.addWidget(main.one.saveButton, 0, 0)

        main.one.visualizeButton = QPushButton('Visualize in 2D')
        grid.addWidget(main.one.visualizeButton, 0, 1)


class OneVisualize(QPlainTextEdit):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 200)
        self.setPlainText('Placeholder\nfor the 1D Visualization.')

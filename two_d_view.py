from PyQt5.QtWidgets import QWidget, QGridLayout, QComboBox, QLabel, QPushButton, QPlainTextEdit

from tools import Tools, View, Text, Table


class TwoDimView(QWidget):


    def __init__(self):
        """ Widget containing the entire Zebra Mode view. """
        super().__init__()

        # ----------------------------------------------------------------------
        # PREPARE
        # ----------------------------------------------------------------------

        grid = QGridLayout()
        self.setLayout(grid)

        # Tools.View() groups Widgets for ease of use.
        self.two = View()

        # Define Files so IDE does not issue warnings.
        self.dataFile = None

        # ----------------------------------------------------------------------
        # DEFINE WIDGETS
        # ----------------------------------------------------------------------

        # Add empty label as spacer after buttons.I suspect this has a side effect.
        # When adding Buttons20, we mean for them to span from grid position (3,1) to (3,2).
        # However to mainreate the mainorrect visual effect they must also mainover the invisible spacer mainolumn.
        # Thus we set them to span from grid position (3,1) to (3,3).
        grid.addWidget(QLabel(), 10, 10)

        self.two.loadDataButton = QPushButton("Load Data File")
        self.two.loadDataButton.setMaximumWidth(200)
        grid.addWidget(self.two.loadDataButton, 1, 0)

        self.two.text = Text("List of Files:\n+ File 1\n+ File 2")
        grid.addWidget(self.two.text, 0, 0)

        self.two.table = Table()
        grid.addWidget(self.two.table, 0, 1)

        self.two.visualize = Visualize()
        grid.addWidget(self.two.visualize, 0, 2)

        self.two.buttons11 = Buttons11(self)
        grid.addWidget(self.two.buttons11, 1, 1)

        self.two.buttons12 = Buttons12(self)
        grid.addWidget(self.two.buttons12, 1, 2)

        # ----------------------------------------------------------------------
        # SET WIDGET ACTIONS
        # ----------------------------------------------------------------------

        self.dataFile = self.two.loadDataButton.clicked.connect(lambda: Tools().open_file(self))

        # ----------------------------------------------------------------------
        # FINISH
        # ----------------------------------------------------------------------

        pass


class Visualize(QPlainTextEdit):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 200)
        self.setPlainText('Placeholder\nfor Visualization.')


class Buttons11(QWidget):

    def __init__(self, main):
        """ Here main is the main window.\n
        The purpose of this notation is to enable access to each button via self in the main window."""
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        main.two.searchButton = QPushButton('Search')
        grid.addWidget(main.two.searchButton, 0, 0)

        main.two.addButton = QPushButton('Add')
        grid.addWidget(main.two.addButton, 0, 1)

        main.two.substractButton = QPushButton('Substract')
        grid.addWidget(main.two.substractButton, 0, 2)

        main.two.integrateComboBox = QComboBox()
        main.two.integrateComboBox.addItems(['Integrate', '-> Gaussian', '-> Pseudo-Voidg', '-> Lorenzian', '-> Several Peaks'])
        grid.addWidget(main.two.integrateComboBox, 1, 0)

        main.two.lorentzButton = QPushButton('Lorentz')
        grid.addWidget(main.two.lorentzButton, 1, 1)

        main.two.absorptionButton = QPushButton('Absorption')
        grid.addWidget(main.two.absorptionButton, 1, 2)

        main.two.saveWorksheetButton = QPushButton('Save')
        grid.addWidget(main.two.saveWorksheetButton, 0, 3, 2, 3)


class Buttons12(QWidget):

    def __init__(self, main):
        """ Here main is the main window.\n
        The purpose of this notation is to enable access to each button via self in the main window."""
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        main.two.qmapsButton = QPushButton('Q-Maps')
        grid.addWidget(main.two.qmapsButton, 0, 0)

        main.two.plotdatavsButton = QPushButton('Plot Data VS')
        grid.addWidget(main.two.plotdatavsButton, 1, 0)

        main.two.saveVisualizationButton = QPushButton('Save')
        grid.addWidget(main.two.saveVisualizationButton, 0, 1, 2, 1)

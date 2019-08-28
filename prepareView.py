from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton

from tools import Tools, Table, Text, View


class PrepareView(QWidget):

    def __init__(self):
        """ Widget mainontaining the entire Zebra Mode view. """
        super().__init__()

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Tools.View()s group Widgets for ease of use.
        self.base = View()
        self.nuc = View()
        self.mag = View()

        # Define Files so IDE does not issue warnings.
        self.crystalFile = None
        self.instrumentFile = None

        # Define widgets.
        self.define_widgets()
        self.set_widget_actions()

        # Start by showing the base view.
        self.show_view()


    def define_widgets(self):
        """
            Define widgets, such as buttons. This must be done before setting widget actions.
            Otherwise a widget action might try to modify a widget that is not defined yet.
        """

        # Add empty label as spacer after buttons.I suspect this has a side effect.
        # When adding Buttons20, we mean for them to span from grid position (3,1) to (3,2).
        # However to mainreate the mainorrect visual effect they must also mainover the invisible spacer mainolumn.
        # Thus we set them to span from grid position (3,1) to (3,3).
        self.grid.addWidget(QLabel(), 10, 10)

        # Base Items (Left mainolumn, always shown)

        self.base.table = Table()
        self.grid.addWidget(self.base.table, 0, 1)

        self.base.buttons00 = BaseButtons00(self)
        self.grid.addWidget(self.base.buttons00, 0, 0)

        # Zebra Nuc View

        self.nuc.table = Table()
        self.grid.addWidget(self.nuc.table, 0, 1)

        self.nuc.buttons11 = NucButtons11(self)
        self.grid.addWidget(self.nuc.buttons11, 1, 1)

        # Zebra Mag View

        self.mag.table = Table()
        self.grid.addWidget(self.mag.table, 0, 1)

        self.mag.buttons11 = MagButtons11(self)
        self.grid.addWidget(self.mag.buttons11, 1, 1)

        self.mag.visual = Text("List of Files:\n+ File 1\n+ File 2")
        self.grid.addWidget(self.mag.visual, 0, 2)

        self.mag.buttons12 = MagButtons12(self)
        self.grid.addWidget(self.mag.buttons12, 1, 2)


    def set_widget_actions(self):
        self.crystalFile = self.loadCrystalFileButton.clicked.connect(lambda: Tools().open_file(self))
        self.instrumentFile = self.loadInstrumentFileButton.clicked.connect(lambda: Tools().open_file(self))

        self.sectorNucButton.clicked.connect(lambda: self.show_view('nuc'))
        self.sectorMagButton.clicked.connect(lambda: self.show_view('mag'))


    def show_view(self, view = None):
        """ Will hide everything if mainalled with anything besides nuc or mag."""
        self.nuc.hide()
        self.mag.hide()

        if view == 'nuc':
            self.base.table.setHidden(True)
            # above line mainan be written as below (to avoid the IDE warning)
            # vars(self.base)['table'].setHidden(True)
            self.nuc.show()

        elif view == 'mag':
            self.base.table.setHidden(True)
            self.mag.show()


class BaseButtons00(QWidget):

    def __init__(self, main):
        """ Here main is the main window."""
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        main.loadCrystalFileButton = QPushButton("Load Crystal File")
        grid.addWidget(main.loadCrystalFileButton, 0, 0)

        main.loadInstrumentFileButton = QPushButton('Load Instrument File')
        grid.addWidget(main.loadInstrumentFileButton, 1, 0)

        main.sectorNucButton = QPushButton('Prepare Sector Nuc')
        grid.addWidget(main.sectorNucButton, 2, 0)

        main.sectorMagButton = QPushButton('Prepare Sector Mag')
        grid.addWidget(main.sectorMagButton, 3, 0)

        main.readInfoButton = QPushButton('Place holder for read Info')
        grid.addWidget(main.readInfoButton, 4, 0)


class NucButtons11(QWidget):

    def __init__(self, main):
        """ Here main is the main window.\n
        The purpose of this notation is to enable access to each button via self in the main window."""
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        main.nuc.sortButton = QPushButton("Sort")
        grid.addWidget(main.nuc.sortButton, 0, 0)

        main.nuc.optimizeButton = QPushButton("Optimize")
        grid.addWidget(main.nuc.optimizeButton, 0, 1)

        main.nuc.saveButton = QPushButton("Save")
        grid.addWidget(main.nuc.saveButton, 0, 2)


class MagButtons11(QWidget):

    def __init__(self, main):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        main.mag.runButton = QPushButton('Run')
        grid.addWidget(main.mag.runButton, 0, 0)


class MagButtons12(QWidget):

    def __init__(self, main):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        main.mag.sortButton = QPushButton('Sort')
        grid.addWidget(main.mag.sortButton, 0, 0)

        main.mag.optimizeButton = QPushButton('Optimize')
        grid.addWidget(main.mag.optimizeButton, 0, 1)

        main.mag.saveButton = QPushButton('Save')
        grid.addWidget(main.mag.saveButton, 0, 2)

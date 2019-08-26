
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QAction, QHBoxLayout, QTabWidget, QTableWidget, QPlainTextEdit


class TwoDimView(QWidget):










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
        self.load_data_button = QPushButton()
        self.load_data_button.setText("Load Data File")
        self.load_data_button.setMaximumWidth(200)
        self.grid.addWidget(self.load_data_button, 1, 0)


        self.one_d_text = OneDText()
        self.grid.addWidget(self.one_d_text, 0,0)


        self.one_d_table = OneDTable()
        self.grid.addWidget(self.one_d_table,0,1)

        self.one_d_visualize = OneDVisualize()
        self.grid.addWidget(self.one_d_visualize,0,2)



        self.buttons20 = Buttons20()
        self.grid.addWidget(self.buttons20, 2,0)

        self.buttons30 = Buttons30()
        self.grid.addWidget(self.buttons30, 3,0)



    def set_widget_actions(self):
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



class OneDVisualize(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200,200)
        self.setPlainText('Placeholder\nfor OneDVisualize().')


class Buttons20(QWidget):

    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout()
        self.setLayout(self.hbox)
        self.sortButton = QPushButton('Sort')
        self.selectButton = QPushButton('Select')
        self.optimizeButton = QPushButton('Optimize')
        self.hbox.addWidget(self.sortButton)
        self.hbox.addWidget(self.selectButton)
        self.hbox.addWidget(self.optimizeButton)




class Buttons30(QWidget):
    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout()
        self.setLayout(self.hbox)


        self.runButton = QPushButton('Run')
        self.saveButton = QPushButton('Save')

        self.hbox.addWidget(self.runButton)
        self.hbox.addWidget(self.saveButton)
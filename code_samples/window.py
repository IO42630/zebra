import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QLabel, QComboBox, QFileDialog
from code_samples.plot_canvas import PlotCanvas

class Window(QMainWindow):
    '''
    How it works:
    First a window is created.
    Then all the widgets (buttons, sliders, plots) are added to the window and hidden.
    Finally depending on what view is requested widgets are shown or hidden.
    This way we work around the need for tabs and maintain a quick and simple UI.
    '''

    def __init__(self):
        super().__init__()

        self.container = QWidget(self)
        self.grid = QGridLayout()

        self.setCentralWidget(self.container)
        self.container.setLayout(self.grid)


        self.define_widgets()
        self.set_widget_actions()
        self.main_view()

        self.setGeometry(0, 0, 500, 300)
        self.setWindowTitle("Zebra")
        self.show()
        sys.exit(app.exec_())


    def define_widgets(self):
        ''' Define widgets such as buttons. This must be done before setting widget actions.
        Otherwise a widget action might try to modify a widget that is not defined yet.'''

        # add empty label as spacer after buttons
        self.grid.addWidget(QLabel(), 10,10)

        self.button_zebra = self.make_button("1 Zebra", self.grid, 0, 0 )
        self.button_back = self.make_button("Back", self.grid, 0,0)
        self.button_dmc = self.make_button("2 DMC", self.grid, 0,1)
        self.button_transfer = self.make_button("3 Transfer\nZebra-DMC-Laue", self.grid,  0,2)


        self.m_range_label = QLabel("Measurement Range:")
        self.grid.addWidget(self.m_range_label, 0, 2)

        self.plot_canvas = PlotCanvas(width = 5, height = 5)
        self.plot_canvas.setFixedWidth(400)
        self.plot_canvas.setFixedHeight(300)
        self.grid.addWidget(self.plot_canvas,0,1,3,1)


        self.m_range_combo = QComboBox()
        self.m_range_combo.addItems(["hkl", "-hkl", "hex", "cub"])

        self.grid.addWidget(self.m_range_combo, 0,3)


        self.add_data_label = QLabel("Add Data:")
        self.grid.addWidget(self.add_data_label,1,2)
        self.add_data_button = self.make_button("Open File", self.grid, 1, 3)

        self.button_zebra13 = self.make_button("1.3", self.grid, 3,3)

        self.button_dmc21 = self.make_button("2.1", self.grid, 0,1)
        self.button_dmc22 = self.make_button("2.2", self.grid, 1,1)



    def set_widget_actions(self):


        # define button actions
        self.button_zebra.clicked.connect(self.zebra_view)
        self.button_back.clicked.connect(self.main_view)
        self.button_dmc.clicked.connect(self.dmc_view)
        self.button_transfer.clicked.connect(self.transfer_view)

        self.m_range_combo.activated[str].connect(self.set_m_range)
        self.add_data_button.clicked.connect(self.open_file)
        self.button_zebra13.clicked.connect(self.zebra13_action)

        self.button_dmc21.clicked.connect(self.dmc21_action)
        self.button_dmc22.clicked.connect(self.dmc22_action)






    def hide_all(self):
        self.button_zebra.setHidden(True)
        self.button_back.setHidden(True)
        self.button_dmc.setHidden(True)
        self.button_transfer.setHidden(True)

        self.m_range_label.setHidden(True)
        self.m_range_combo.setHidden(True)


        self.plot_canvas.setHidden(True)
        self.add_data_label.setHidden(True)
        self.add_data_button.setHidden(True)
        self.button_zebra13.setHidden(True)

        self.button_dmc21.setHidden(True)
        self.button_dmc22.setHidden(True)



    def main_view(self):
        self.hide_all()
        self.button_zebra.setHidden(False)
        self.button_dmc.setHidden(False)
        self.button_transfer.setHidden(False)




    def zebra_view(self):
        self.hide_all()
        self.button_back.setHidden(False)

        self.plot_canvas.setHidden(False)

        self.m_range_label.setHidden(False)
        self.m_range_combo.setHidden(False)

        self.add_data_label.setHidden(False)
        self.add_data_button.setHidden(False)

        self.button_zebra13.setHidden(False)

    def dmc_view(self):
        self.hide_all()
        self.button_back.setHidden(False)
        self.button_dmc21.setHidden(False)
        self.button_dmc22.setHidden(False)



    def transfer_view(self):
        self.hide_all()
        self.button_back.setHidden(False)



    def open_file(self):
        ''' Corresponds to 1.2
        TODO Right now this is just copy&pasted. Clean this up.'''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        pass

    def zebra13_action(self):
        pass

    def dmc21_action(self):
        pass

    def dmc22_action(self):
        pass

    def set_m_range(self, selection):
        ''' Corresponds to 1.1'''
        print(selection)
        pass







    def make_button(self, text, grid, row, col):
        """Create a button in the grid and hide it."""
        button = QPushButton(self)
        button.setText(text)
        grid.addWidget(button, row, col)
        button.setHidden(True)
        button.setFixedHeight(50)
        button.setFixedWidth(150)
        return button







if __name__ == '__main__':
    app = QApplication(sys.argv)
    hello = Window()
    sys.exit(app.exec())



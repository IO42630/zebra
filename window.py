import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QLabel, QSpacerItem, QSizePolicy, QComboBox


class Window(QMainWindow):

    def __init__(self):



        super().__init__()

        container = QWidget(self)
        self.setCentralWidget(container)

        grid = QGridLayout()
        # add empty label as spacer after buttons
        grid.addWidget(QLabel(), 10,10)
        container.setLayout(grid)


        # define buttons
        self.button_zebra = self.make_button("1 Zebra", grid, 0, 0 )
        self.button_back = self.make_button("Back", grid, 0,0)
        self.button_dmc = self.make_button("2 DMC", grid, 0,1)
        self.button_transfer = self.make_button("3 Transfer\nZebra-DMC-Laue", grid,  0,2)


        self.m_range_label = QLabel("Measurement Range:")
        grid.addWidget(self.m_range_label, 0, 1)



        self.m_range_combo = QComboBox()
        self.m_range_combo.addItem("hkl")
        self.m_range_combo.addItem("-hkl")
        self.m_range_combo.addItem("hex")
        self.m_range_combo.addItem("cub")

        grid.addWidget(self.m_range_combo, 0,2)

        self.button_zebra12 = self.make_button("1.2", grid, 1,1)
        self.button_zebra13 = self.make_button("1.3", grid, 3,1)

        self.button_dmc21 = self.make_button("2.1", grid, 0,1)
        self.button_dmc22 = self.make_button("2.2", grid, 1,1)



        # define button actions
        self.button_zebra.clicked.connect(self.zebra_view)
        self.button_back.clicked.connect(self.main_view)
        self.button_dmc.clicked.connect(self.dmc_view)
        self.button_transfer.clicked.connect(self.transfer_view)

        self.m_range_combo.activated[str].connect(self.set_m_range)
        self.button_zebra12.clicked.connect(self.zebra12_action)
        self.button_zebra13.clicked.connect(self.zebra13_action)

        self.button_dmc21.clicked.connect(self.dmc21_action)
        self.button_dmc22.clicked.connect(self.dmc22_action)


        self.main_view()
        self.setGeometry(0, 0, 500, 300)
        self.setWindowTitle("Zebra")
        self.show()
        sys.exit(app.exec_())


    def hide_all(self):
        self.button_zebra.setHidden(True)
        self.button_back.setHidden(True)
        self.button_dmc.setHidden(True)
        self.button_transfer.setHidden(True)

        self.m_range_label.setHidden(True)
        self.m_range_combo.setHidden(True)
        self.button_zebra12.setHidden(True)
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

        self.m_range_label.setHidden(False)
        self.m_range_combo.setHidden(False)
        self.button_zebra12.setHidden(False)
        self.button_zebra13.setHidden(False)

    def dmc_view(self):
        self.hide_all()
        self.button_back.setHidden(False)
        self.button_dmc21.setHidden(False)
        self.button_dmc22.setHidden(False)



    def transfer_view(self):
        self.hide_all()
        self.button_back.setHidden(False)


    def zebra11_action(self):
        pass

    def zebra12_action(self):
        pass

    def zebra13_action(self):
        pass

    def dmc21_action(self):
        pass

    def dmc22_action(self):
        pass

    def set_m_range(self, selection):
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



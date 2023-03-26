from PySide2.QtWidgets import QWidget, QPushButton

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main widget")

        button = QPushButton("Press me", self)
        button.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        #print("Clicked!")
         self.close()


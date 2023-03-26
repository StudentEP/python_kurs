from PySide2.QtWidgets import QWidget, QPushButton, QLineEdit,\
    QLabel, QVBoxLayout, QMessageBox


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main widget")


        button = QPushButton("Press me!", self)
        button.clicked.connect(self.onButtonClicked)


        self. edit = QLineEdit(self)


        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(button)

    def onButtonClicked(self):
        editText = self.edit.text()
        self.label.setText(editText)
        QMessageBox.critical(self, "Info", editText)


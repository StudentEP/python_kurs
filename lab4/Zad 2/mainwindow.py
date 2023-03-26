from PySide2.QtWidgets import *




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main widget")
        self.initializeMenu()








    def initializeMenu(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        newAction = fileMenu.addAction("New")
        openAction = fileMenu.addAction("Open")
        saveAction = fileMenu.addAction("Save")
        saveAsAction = fileMenu.addAction("Save as")


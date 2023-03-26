from PySide2.QtWidgets import *




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main widget")
        self.initializeMenu()

        self.edit = QTextEdit(self)
        self.setCentralWidget(self.edit)




    def initializeMenu(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        newAction = fileMenu.addAction("New")
        openAction = fileMenu.addAction("Open")
        saveAction = fileMenu.addAction("Save")
        saveAsAction = fileMenu.addAction("Save as")
        newAction.triggered.connect(self.onNewAction)
        openAction.triggered.connect(self.onOpenAction)

    def onNewAction(self):
        self.edit.clear ()

    def onOpenAction(self):
        path,_ = QFileDialog.getOpenFileName(self, "Open file","")
        if len(path)>0:
            file = open(path, 'r')
            data = file.read()
            self.edit.setText(data)

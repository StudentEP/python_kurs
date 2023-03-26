from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from mainwindow import MainWindow

def main():
    app = QApplication([])

    window = MainWindow()
    window.show()


    app.exec_()



if __name__ == "__main__":
    main()
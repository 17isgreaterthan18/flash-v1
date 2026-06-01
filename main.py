import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Hello world!')

        self.button = QPushButton("Push me!")
        self.button.clicked.connect(self.button_press)
        self.setCentralWidget(self.button)

    def button_press(self):
        self.button.setText("Clicked!")

if __name__ == "__main__":
    main()

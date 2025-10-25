from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout
import src.utils.settings as settings

class MainWindow(QMainWindow):
    settings = settings.Settings("setting.json")

    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.settings.app_name)
        self.layout = QVBoxLayout()
        self.setGeometry(100, 100, self.settings.starting_size.width, self.settings.starting_size.height)

    def bindWidgets(self):
        # Create and attach and such widgets here?
        pushButton = QPushButton("Test Button", self)
        pushButton.setLayout(self.layout)
        pushButton.setFixedHeight(40)
        pushButton.setFixedWidth(120)
        self.setCentralWidget(pushButton)

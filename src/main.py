from PyQt5.QtWidgets import QApplication, QWidget as Widget, QMainWindow

import src.utils.settings as settings
import src.frontend.main_window as MainWindow

import sys


# Load settings from JSON file
settings = settings.Settings("setting.json")

# Initialize the application
app = QApplication(sys.argv)

# Create and show the main window
mainWindow = MainWindow.MainWindow()
mainWindow.bindWidgets()
mainWindow.show()

# Start the application's event loop
app.exec()